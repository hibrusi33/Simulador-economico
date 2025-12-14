// GlobeSelector.jsx
import { useEffect, useRef, useState, useCallback, useMemo } from 'react';
import Globe from 'react-globe.gl';
import { interpolateRgb } from 'd3-interpolate';

const GlobeSelector = ({ 
  onSelectCountry, 
  currentMonthData = {}, 
  selectedCountries = [],
  isSimulationRunning = false 
}) => {
  const globeEl = useRef();
  const [countries, setCountries] = useState({ features: [] });
  const [polygonsData, setPolygonsData] = useState([]);
  const [hoverD, setHoverD] = useState();

  // Cargar datos GeoJSON de países
  useEffect(() => {
    fetch('https://raw.githubusercontent.com/vasturiano/react-globe.gl/master/example/datasets/ne_110m_admin_0_countries.geojson')
      .then(res => res.json())
      .then(data => {
        setCountries(data);
        setPolygonsData(data.features);
      })
      .catch(err => console.error('Error cargando GeoJSON:', err));
  }, []);

  // Auto-rotación del globo
  useEffect(() => {
    if (globeEl.current && !isSimulationRunning) {
      const controls = globeEl.current.controls();
      controls.autoRotate = true;
      controls.autoRotateSpeed = 0.5;
    }
  }, [isSimulationRunning]);

  // Recrear polygonsData solo cuando hay cambios (optimizado)
  useEffect(() => {
    if (countries.features && countries.features.length > 0) {
      setPolygonsData([...countries.features]);
    }
  }, [currentMonthData, countries.features]);


  // Mapeo de códigos ISO a códigos de backend - MEMOIZADO para evitar recreación
  const isoToBackendCode = useMemo(() => ({
    'USA': 'USA', 'CHN': 'China', 'RUS': 'Russia', 'DEU': 'Germany', 'JPN': 'Japan',
    'ESP': 'Spain', 'IND': 'India', 'BRA': 'Brazil', 'SAU': 'SaudiArabia', 'FRA': 'France',
    'GBR': 'UK', 'MEX': 'Mexico', 'KOR': 'SouthKorea', 'AUS': 'Australia', 'CAN': 'Canada',
    'ITA': 'Italy', 'ARG': 'Argentina', 'TUR': 'Turkey', 'IDN': 'Indonesia', 'NGA': 'Nigeria',
    'EGY': 'Egypt', 'POL': 'Poland', 'THA': 'Thailand', 'NLD': 'Netherlands', 'ZAF': 'SouthAfrica',
    'NOR': 'Norway', 'SWE': 'Sweden', 'FIN': 'Finland', 'DNK': 'Denmark', 'BEL': 'Belgium',
    'CHE': 'Switzerland', 'AUT': 'Austria', 'PRT': 'Portugal', 'GRC': 'Greece', 'CZE': 'Czech',
    'ROU': 'Romania', 'HUN': 'Hungary', 'IRL': 'Ireland', 'UKR': 'Ukraine', 'VNM': 'Vietnam',
    'PHL': 'Philippines', 'MYS': 'Malaysia', 'SGP': 'Singapore', 'BGD': 'Bangladesh', 'PAK': 'Pakistan',
    'NZL': 'NewZealand', 'TWN': 'Taiwan', 'HKG': 'HongKong', 'PRK': 'NorthKorea', 'COL': 'Colombia',
    'CHL': 'Chile', 'PER': 'Peru', 'VEN': 'Venezuela', 'ECU': 'Ecuador', 'CUB': 'Cuba',
    'KEN': 'Kenya', 'ETH': 'Ethiopia', 'GHA': 'Ghana', 'MAR': 'Morocco', 'DZA': 'Algeria',
    'IRN': 'Iran', 'ARE': 'UAE', 'ISR': 'Israel', 'QAT': 'Qatar', 'KWT': 'Kuwait',
    'IRQ': 'Iraq', 'SYR': 'Syria', 'JOR': 'Jordan', 'LBN': 'Lebanon', 'OMN': 'Oman',
    'YEM': 'Yemen', 'BHR': 'Bahrain', 'SRB': 'Serbia', 'HRV': 'Croatia', 'BGR': 'Bulgaria',
    'SVK': 'Slovakia', 'SVN': 'Slovenia', 'LTU': 'Lithuania', 'LVA': 'Latvia', 'EST': 'Estonia',
    'BLR': 'Belarus', 'ISL': 'Iceland', 'LUX': 'Luxembourg', 'CYP': 'Cyprus', 'MLT': 'Malta',
    'MMR': 'Myanmar', 'KHM': 'Cambodia', 'LAO': 'Laos', 'NPL': 'Nepal', 'LKA': 'SriLanka',
    'AFG': 'Afghanistan', 'KAZ': 'Kazakhstan', 'UZB': 'Uzbekistan', 'MNG': 'Mongolia', 'URY': 'Uruguay',
    'PRY': 'Paraguay', 'BOL': 'Bolivia', 'CRI': 'CostaRica', 'PAN': 'Panama', 'GTM': 'Guatemala',
    'DOM': 'DominicanRep', 'TZA': 'Tanzania', 'UGA': 'Uganda', 'CMR': 'Cameroon', 'CIV': 'IvoryCoast',
    'SEN': 'Senegal', 'AGO': 'Angola', 'TUN': 'Tunisia', 'LBY': 'Libya', 'ZWE': 'Zimbabwe',
    'MDG': 'Madagascar', 'MOZ': 'Mozambique', 'ZMB': 'Zambia', 'NAM': 'Namibia', 'BWA': 'Botswana',
    'SDN': 'Sudan', 'SSD': 'SouthSudan', 'SOM': 'Somalia', 'COG': 'Congo', 'COD': 'DRC',
    'PNG': 'PapuaNewGuinea', 'GRL': 'Greenland', 'ATA': 'Antarctica', 'ALB': 'Albania', 'MKD': 'NorthMacedonia',
    'BIH': 'Bosnia', 'MNE': 'Montenegro', 'MDA': 'Moldova', 'ARM': 'Armenia', 'GEO': 'Georgia',
    'AZE': 'Azerbaijan', 'TKM': 'Turkmenistan', 'KGZ': 'Kyrgyzstan', 'TJK': 'Tajikistan', 'TLS': 'TimorLeste',
    'BRN': 'Brunei', 'MDV': 'Maldives', 'BTN': 'Bhutan', 'BLZ': 'Belize', 'SLV': 'ElSalvador',
    'HND': 'Honduras', 'NIC': 'Nicaragua', 'JAM': 'Jamaica', 'HTI': 'Haiti', 'TTO': 'TrinidadTobago',
    'BHS': 'Bahamas', 'BRB': 'Barbados', 'GUY': 'Guyana', 'SUR': 'Suriname', 'TCD': 'Chad',
    'MLI': 'Mali', 'NER': 'Niger', 'BFA': 'BurkinaFaso', 'RWA': 'Rwanda', 'BDI': 'Burundi',
    'ERI': 'Eritrea', 'LBR': 'Liberia', 'SLE': 'SierraLeone', 'GIN': 'Guinea', 'TGO': 'Togo',
    'BEN': 'Benin', 'MRT': 'Mauritania', 'GMB': 'Gambia', 'GAB': 'Gabon', 'CAF': 'CAR',
    'MWI': 'Malawi', 'LSO': 'Lesotho', 'SWZ': 'Eswatini', 'DJI': 'Djibouti', 'MUS': 'Mauritius',
    'FJI': 'Fiji', 'SLB': 'SolomonIslands', 'VUT': 'Vanuatu', 'WSM': 'Samoa', 'TON': 'Tonga'
  }), []);

  // Obtener código del país desde ISO - MEMOIZADO
  const getCountryCode = useCallback((isoCode) => {
    return isoToBackendCode[isoCode] || null;
  }, [isoToBackendCode]);

  // Helper: Obtener color basado en cambio de PIB (optimizado con cache)
  const getColorFromPIBChange = useCallback((cambioRelativo) => {
    if (cambioRelativo < -0.20) return '#7f1d1d';
    if (cambioRelativo < -0.05) {
      const t = (cambioRelativo + 0.20) / 0.15;
      return interpolateRgb('#7f1d1d', '#ef4444')(t);
    }
    if (cambioRelativo < 0.05) {
      const t = (cambioRelativo + 0.05) / 0.10;
      return interpolateRgb('#ef4444', '#fbbf24')(t);
    }
    if (cambioRelativo < 0.20) {
      const t = (cambioRelativo - 0.05) / 0.15;
      return interpolateRgb('#fbbf24', '#34d399')(t);
    }
    return '#10b981';
  }, []);

  // Calcular altitud basada en PIB (optimizada)
  const getPolygonAltitude = useCallback((d) => {
    const countryCode = getCountryCode(d.properties.ISO_A3);
    if (!countryCode || !currentMonthData[countryCode]) return 0.01;

    const data = currentMonthData[countryCode];
    const cambioRelativo = ((data.PIB || 1000) - (data.pib_inicial || 1000)) / (data.pib_inicial || 1000);
    const altitude = 0.02 + cambioRelativo * 0.50;

    return Math.max(0.01, Math.min(0.40, altitude));
  }, [currentMonthData, getCountryCode]);

  // Color de superficie y bordes (mismo color, optimizado)
  const getPolygonColor = useCallback((d) => {
    const countryCode = getCountryCode(d.properties.ISO_A3);

    // Simulación activa: color por PIB
    if (countryCode && currentMonthData[countryCode]) {
      const data = currentMonthData[countryCode];
      const cambioRelativo = ((data.PIB || 1000) - (data.pib_inicial || 1000)) / (data.pib_inicial || 1000);
      return getColorFromPIBChange(cambioRelativo);
    }

    // Hover (solo sin simulación)
    if (hoverD && d === hoverD) return '#a78bfa';

    // Seleccionado sin datos
    if (countryCode && selectedCountries.includes(countryCode)) return '#60a5fa';

    // País no disponible
    return '#1e293b';
  }, [currentMonthData, hoverD, selectedCountries, getCountryCode, getColorFromPIBChange]);

  // Manejar clic en país
  const handleCountryClick = (polygon) => {
    if (!polygon || !polygon.properties) return;
    
    const isoCode = polygon.properties.ISO_A3;
    const countryCode = getCountryCode(isoCode);
    const countryName = polygon.properties.ADMIN;
    
    if (countryCode && onSelectCountry) {
      onSelectCountry(countryCode, countryName);
    }
  };

  // Label para países (optimizado)
  const getPolygonLabel = useCallback((d) => {
    const countryCode = getCountryCode(d.properties.ISO_A3);
    const countryName = d.properties.ADMIN;

    if (!countryCode || !currentMonthData[countryCode]) {
      return `<div style="color: white; background: rgba(0,0,0,0.8); padding: 8px; border-radius: 4px; font-family: monospace;">
        ${countryName}<br/>
        <span style="color: #666;">No disponible</span>
      </div>`;
    }

    const data = currentMonthData[countryCode];
    const pibChange = data.pib_inicial
      ? (((data.PIB / data.pib_inicial) - 1) * 100).toFixed(1)
      : 0;

    return `<div style="color: #e2e8f0; background: #1e293b; padding: 10px; border-radius: 6px; font-family: monospace; border: 2px solid #60a5fa;">
      <div style="font-size: 14px; font-weight: bold; color: #60a5fa; margin-bottom: 4px;">${countryName}</div>
      <div style="font-size: 11px; color: #94a3b8; margin-bottom: 6px;">${data.ideologia || 'N/A'}</div>
      <div style="font-size: 12px;">
        <div style="color: #60a5fa;">PIB: $${data.PIB?.toFixed(0)} B (${pibChange > 0 ? '+' : ''}${pibChange}%)</div>
        <div style="color: ${data.Bienestar > 60 ? '#34d399' : data.Bienestar > 40 ? '#fbbf24' : '#ef4444'};">
          Bienestar: ${data.Bienestar?.toFixed(0)}/100
        </div>
        <div style="color: ${data.Libertad > 60 ? '#34d399' : data.Libertad > 40 ? '#fbbf24' : '#ef4444'};">
          Libertad: ${data.Libertad?.toFixed(0)}/100
        </div>
      </div>
    </div>`;
  }, [currentMonthData, getCountryCode]);

  return (
    <div className="relative w-full h-full flex items-center justify-center" style={{ backgroundColor: 'var(--color-bg-dark)' }}>
      <Globe
        ref={globeEl}

        // Datos
        polygonsData={polygonsData}

        // Apariencia del globo
        globeImageUrl="//unpkg.com/three-globe/example/img/earth-night.jpg"
        backgroundImageUrl="//unpkg.com/three-globe/example/img/night-sky.png"

        // Atmósfera con nuevo color
        atmosphereColor="#60a5fa"
        atmosphereAltitude={0.15}

        // Configuración de polígonos (países)
        polygonAltitude={getPolygonAltitude}
        polygonCapColor={getPolygonColor}
        polygonSideColor={getPolygonColor}
        polygonStrokeColor={() => '#1e293b'}
        polygonLabel={getPolygonLabel}

        // Animación suave entre meses (reducida para mejor rendimiento)
        polygonsTransitionDuration={300}

        // Interactividad
        onPolygonClick={handleCountryClick}
        onPolygonHover={setHoverD}

        // Controles
        enablePointerInteraction={true}

        // Tamaño del globo
        width={undefined}
        height={undefined}
      />

      {/* Leyenda de colores */}
      <div className="absolute bottom-6 right-6 rounded-lg p-4 font-mono text-xs backdrop-blur-sm" style={{ backgroundColor: 'var(--color-bg-card)', border: '1px solid var(--color-border)' }}>
        <div className="font-bold mb-2 text-sm" style={{ color: 'var(--color-primary)' }}>LEYENDA</div>

        {/* Colores = PIB */}
        <div className="mb-2">
          <div className="text-xs font-semibold mb-1" style={{ color: '#94a3b8' }}>Color del país (cambio PIB):</div>
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded" style={{ backgroundColor: '#10b981' }}></div>
              <span style={{ color: 'var(--color-text)', fontSize: '11px' }}>+20% o más</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded" style={{ backgroundColor: '#34d399' }}></div>
              <span style={{ color: 'var(--color-text)', fontSize: '11px' }}>+5% a +20%</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded" style={{ backgroundColor: '#fbbf24' }}></div>
              <span style={{ color: 'var(--color-text)', fontSize: '11px' }}>±5% (estable)</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded" style={{ backgroundColor: '#ef4444' }}></div>
              <span style={{ color: 'var(--color-text)', fontSize: '11px' }}>-5% a -20%</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded" style={{ backgroundColor: '#7f1d1d' }}></div>
              <span style={{ color: 'var(--color-text)', fontSize: '11px' }}>-20% o menos</span>
            </div>
          </div>
        </div>
      </div>

      {/* Indicador de carga */}
      {polygonsData.length === 0 && (
        <div className="absolute inset-0 flex items-center justify-center" style={{ backgroundColor: 'rgba(15, 23, 42, 0.7)' }}>
          <div className="font-mono text-xl animate-pulse" style={{ color: 'var(--color-primary)' }}>
            CARGANDO MAPA DEL MUNDO...
          </div>
        </div>
      )}
    </div>
  );
};

export default GlobeSelector;
