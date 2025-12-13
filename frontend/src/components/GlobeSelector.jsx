// GlobeSelector.jsx
import { useEffect, useRef, useState } from 'react';
import Globe from 'react-globe.gl';
import * as d3 from 'd3-scale-chromatic';

const GlobeSelector = ({ 
  onSelectCountry, 
  currentMonthData = {}, 
  selectedCountries = [],
  isSimulationRunning = false 
}) => {
  const globeEl = useRef();
  const [countries, setCountries] = useState({ features: [] });
  const [hoverD, setHoverD] = useState();
  const [, forceUpdate] = useState({});

  // Cargar datos GeoJSON de países
  useEffect(() => {
    fetch('https://raw.githubusercontent.com/vasturiano/react-globe.gl/master/example/datasets/ne_110m_admin_0_countries.geojson')
      .then(res => res.json())
      .then(data => {
        setCountries(data);
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

  // Forzar actualización cuando cambian los datos del mes
  useEffect(() => {
    if (Object.keys(currentMonthData).length > 0) {
      forceUpdate({});
    }
  }, [currentMonthData]);

  // Mapeo de códigos ISO a códigos de backend
  const isoToBackendCode = {
    // Originales
    'USA': 'USA',
    'CHN': 'China',
    'RUS': 'Russia',
    'DEU': 'Germany',
    'JPN': 'Japan',
    'ESP': 'Spain',
    'IND': 'India',
    'BRA': 'Brazil',
    'SAU': 'SaudiArabia',
    'FRA': 'France',
    'GBR': 'UK',
    'MEX': 'Mexico',
    'KOR': 'SouthKorea',
    'AUS': 'Australia',
    'CAN': 'Canada',
    'ITA': 'Italy',
    'ARG': 'Argentina',
    'TUR': 'Turkey',
    'IDN': 'Indonesia',
    'NGA': 'Nigeria',
    'EGY': 'Egypt',
    'POL': 'Poland',
    'THA': 'Thailand',
    'NLD': 'Netherlands',
    'ZAF': 'SouthAfrica',
    // Europa
    'NOR': 'Norway',
    'SWE': 'Sweden',
    'FIN': 'Finland',
    'DNK': 'Denmark',
    'BEL': 'Belgium',
    'CHE': 'Switzerland',
    'AUT': 'Austria',
    'PRT': 'Portugal',
    'GRC': 'Greece',
    'CZE': 'Czech',
    'ROU': 'Romania',
    'HUN': 'Hungary',
    'IRL': 'Ireland',
    'UKR': 'Ukraine',
    // Asia-Pacífico
    'VNM': 'Vietnam',
    'PHL': 'Philippines',
    'MYS': 'Malaysia',
    'SGP': 'Singapore',
    'BGD': 'Bangladesh',
    'PAK': 'Pakistan',
    'NZL': 'NewZealand',
    'TWN': 'Taiwan',
    'HKG': 'HongKong',
    'PRK': 'NorthKorea',
    // América
    'COL': 'Colombia',
    'CHL': 'Chile',
    'PER': 'Peru',
    'VEN': 'Venezuela',
    'ECU': 'Ecuador',
    'CUB': 'Cuba',
    // África
    'KEN': 'Kenya',
    'ETH': 'Ethiopia',
    'GHA': 'Ghana',
    'MAR': 'Morocco',
    'DZA': 'Algeria',
    // Medio Oriente
    'IRN': 'Iran',
    'ARE': 'UAE',
    'ISR': 'Israel',
    'QAT': 'Qatar',
    'KWT': 'Kuwait',
    'IRQ': 'Iraq',
    'SYR': 'Syria',
    'JOR': 'Jordan',
    'LBN': 'Lebanon',
    'OMN': 'Oman',
    'YEM': 'Yemen',
    'BHR': 'Bahrain',
    // Europa adicional
    'SRB': 'Serbia',
    'HRV': 'Croatia',
    'BGR': 'Bulgaria',
    'SVK': 'Slovakia',
    'SVN': 'Slovenia',
    'LTU': 'Lithuania',
    'LVA': 'Latvia',
    'EST': 'Estonia',
    'BLR': 'Belarus',
    'ISL': 'Iceland',
    'LUX': 'Luxembourg',
    'CYP': 'Cyprus',
    'MLT': 'Malta',
    // Asia adicional
    'MMR': 'Myanmar',
    'KHM': 'Cambodia',
    'LAO': 'Laos',
    'NPL': 'Nepal',
    'LKA': 'SriLanka',
    'AFG': 'Afghanistan',
    'KAZ': 'Kazakhstan',
    'UZB': 'Uzbekistan',
    'MNG': 'Mongolia',
    // América adicional
    'URY': 'Uruguay',
    'PRY': 'Paraguay',
    'BOL': 'Bolivia',
    'CRI': 'CostaRica',
    'PAN': 'Panama',
    'GTM': 'Guatemala',
    'DOM': 'DominicanRep',
    // África adicional
    'TZA': 'Tanzania',
    'UGA': 'Uganda',
    'CMR': 'Cameroon',
    'CIV': 'IvoryCoast',
    'SEN': 'Senegal',
    'AGO': 'Angola',
    'TUN': 'Tunisia',
    'LBY': 'Libya',
    'ZWE': 'Zimbabwe',
    'MDG': 'Madagascar',
    'MOZ': 'Mozambique',
    'ZMB': 'Zambia',
    'NAM': 'Namibia',
    'BWA': 'Botswana',
    'SDN': 'Sudan',
    'SSD': 'SouthSudan',
    'SOM': 'Somalia',
    'COG': 'Congo',
    'COD': 'DRC',
    // Oceanía
    'PNG': 'PapuaNewGuinea',
    // Territorios especiales
    'GRL': 'Greenland'
  };

  // Obtener código del país desde ISO
  const getCountryCode = (isoCode) => {
    return isoToBackendCode[isoCode] || null;
  };

  // Calcular altitud basada en PIB
  const getPolygonAltitude = (d) => {
    const countryCode = getCountryCode(d.properties.ISO_A3);

    if (!countryCode || !currentMonthData[countryCode]) {
      return 0.01;
    }

    const data = currentMonthData[countryCode];
    const pibActual = data.PIB || 1000;
    const pibInicial = data.pib_inicial || 1000;

    // Altura base cuando PIB = PIB inicial
    const alturaBase = 0.02;

    // Calcular cambio relativo (diferencia porcentual desde PIB inicial)
    const cambioRelativo = (pibActual - pibInicial) / pibInicial;

    // MULTIPLICADOR ALTO: hace que los cambios sean MUY visibles
    // ±10% PIB = ±0.05 altura, ±50% PIB = ±0.25 altura
    const deltaAltura = cambioRelativo * 0.50;

    // Altura final: base + cambio (limitado entre 0.001 y 0.35)
    const altitude = Math.max(0.001, Math.min(0.35, alturaBase + deltaAltura));

    return altitude;
  };

  // Calcular color basado en Bienestar (verde = alto, rojo = bajo)
  const getPolygonColor = (d) => {
    const countryCode = getCountryCode(d.properties.ISO_A3);

    // Si el país tiene datos de simulación activa, SIEMPRE usar color basado en bienestar
    if (countryCode && currentMonthData[countryCode]) {
      const data = currentMonthData[countryCode];
      const bienestar = data.Bienestar || 50;

      // Interpolación de color: Rojo suave -> Verde menta
      if (bienestar < 50) {
        // Rojo suave a Amarillo suave
        const t = bienestar / 50;
        return d3.interpolateRgb('#ef4444', '#fbbf24')(t);
      } else {
        // Amarillo suave a Verde menta
        const t = (bienestar - 50) / 50;
        return d3.interpolateRgb('#fbbf24', '#34d399')(t);
      }
    }

    // Hover effect SOLO si NO hay simulación activa
    if (hoverD && d === hoverD) {
      return '#a78bfa';
    }

    // Si está seleccionado pero no tiene datos de simulación, mostrar azul
    if (countryCode && selectedCountries.includes(countryCode)) {
      return '#60a5fa';
    }

    // Países no disponibles: gris oscuro
    return '#1e293b';
  };

  // Color de los lados del polígono - muestra si PIB sube (verde) o baja (rojo)
  const getPolygonSideColor = (d) => {
    const countryCode = getCountryCode(d.properties.ISO_A3);

    if (!countryCode || !currentMonthData[countryCode]) {
      return 'rgba(96, 165, 250, 0.3)'; // Azul translúcido por defecto
    }

    const data = currentMonthData[countryCode];
    const pibActual = data.PIB || 1000;
    const pibInicial = data.pib_inicial || 1000;
    const cambioRelativo = (pibActual - pibInicial) / pibInicial;

    if (cambioRelativo > 0.02) {
      // PIB subiendo > 2%: Verde brillante
      return 'rgba(52, 211, 153, 0.8)';
    } else if (cambioRelativo < -0.02) {
      // PIB bajando > 2%: Rojo brillante
      return 'rgba(239, 68, 68, 0.8)';
    } else {
      // PIB estable ±2%: Amarillo suave
      return 'rgba(251, 191, 36, 0.6)';
    }
  };

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

  // Label para países seleccionados
  const getPolygonLabel = (d) => {
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
  };

  return (
    <div className="relative w-full h-full flex items-center justify-center" style={{ backgroundColor: 'var(--color-bg-dark)' }}>
      <Globe
        ref={globeEl}

        // Datos
        polygonsData={countries.features}

        // Apariencia del globo
        globeImageUrl="//unpkg.com/three-globe/example/img/earth-night.jpg"
        backgroundImageUrl="//unpkg.com/three-globe/example/img/night-sky.png"

        // Atmósfera con nuevo color
        atmosphereColor="#60a5fa"
        atmosphereAltitude={0.15}

        // Configuración de polígonos (países)
        polygonAltitude={getPolygonAltitude}
        polygonCapColor={getPolygonColor}
        polygonSideColor={getPolygonSideColor}
        polygonStrokeColor={() => '#1e293b'}
        polygonLabel={getPolygonLabel}

        // Animación suave entre meses
        polygonsTransitionDuration={1000}

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

        {/* Colores superiores = Bienestar */}
        <div className="mb-2">
          <div className="text-xs font-semibold mb-1" style={{ color: '#94a3b8' }}>Superficie:</div>
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded" style={{ backgroundColor: '#34d399' }}></div>
              <span style={{ color: 'var(--color-text)', fontSize: '11px' }}>Alto Bienestar</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded" style={{ backgroundColor: '#fbbf24' }}></div>
              <span style={{ color: 'var(--color-text)', fontSize: '11px' }}>Medio</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded" style={{ backgroundColor: '#ef4444' }}></div>
              <span style={{ color: 'var(--color-text)', fontSize: '11px' }}>Bajo</span>
            </div>
          </div>
        </div>

        {/* Bordes = PIB */}
        <div className="pt-2" style={{ borderTop: '1px solid var(--color-border)' }}>
          <div className="text-xs font-semibold mb-1" style={{ color: '#94a3b8' }}>Bordes (PIB):</div>
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded" style={{ backgroundColor: '#34d399', opacity: 0.8 }}></div>
              <span style={{ color: 'var(--color-text)', fontSize: '11px' }}>↑ Subiendo</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded" style={{ backgroundColor: '#fbbf24', opacity: 0.6 }}></div>
              <span style={{ color: 'var(--color-text)', fontSize: '11px' }}>≈ Estable</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-3 h-3 rounded" style={{ backgroundColor: '#ef4444', opacity: 0.8 }}></div>
              <span style={{ color: 'var(--color-text)', fontSize: '11px' }}>↓ Bajando</span>
            </div>
          </div>
        </div>
      </div>

      {/* Indicador de carga */}
      {countries.features.length === 0 && (
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
