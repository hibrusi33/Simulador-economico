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
    'KWT': 'Kuwait'
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
    
    // Normalizar: PIB actual / PIB inicial
    // Rango: 0.01 (muy bajo) a 0.15 (muy alto)
    const ratio = pibActual / pibInicial;
    const altitude = Math.max(0.01, Math.min(0.15, ratio * 0.05));
    
    return altitude;
  };

  // Calcular color basado en Bienestar (verde = alto, rojo = bajo)
  const getPolygonColor = (d) => {
    const countryCode = getCountryCode(d.properties.ISO_A3);

    // País seleccionado: azul primario brillante
    if (selectedCountries.includes(countryCode)) {
      return '#60a5fa';
    }

    // Hover effect
    if (hoverD && d === hoverD) {
      return '#a78bfa';
    }

    if (!countryCode || !currentMonthData[countryCode]) {
      // Países no simulados: gris oscuro
      return '#1e293b';
    }

    const data = currentMonthData[countryCode];
    const bienestar = data.Bienestar || 50;

    // Interpolación de color: Rojo suave -> Verde menta
    let color;
    if (bienestar < 50) {
      // Rojo suave a Amarillo suave
      const t = bienestar / 50;
      color = d3.interpolateRgb('#ef4444', '#fbbf24')(t);
    } else {
      // Amarillo suave a Verde menta
      const t = (bienestar - 50) / 50;
      color = d3.interpolateRgb('#fbbf24', '#34d399')(t);
    }

    return color;
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
        polygonSideColor={() => 'rgba(96, 165, 250, 0.3)'}
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
      <div className="absolute bottom-6 right-6 rounded-lg p-4 font-mono text-sm backdrop-blur-sm" style={{ backgroundColor: 'var(--color-bg-card)', border: '1px solid var(--color-border)' }}>
        <div className="font-bold mb-2" style={{ color: 'var(--color-primary)' }}>LEYENDA</div>
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 rounded" style={{ backgroundColor: '#34d399' }}></div>
            <span style={{ color: 'var(--color-text)' }}>Alto Bienestar</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 rounded" style={{ backgroundColor: '#fbbf24' }}></div>
            <span style={{ color: 'var(--color-text)' }}>Medio Bienestar</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 rounded" style={{ backgroundColor: '#ef4444' }}></div>
            <span style={{ color: 'var(--color-text)' }}>Bajo Bienestar</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 rounded" style={{ backgroundColor: '#60a5fa' }}></div>
            <span style={{ color: 'var(--color-text)' }}>Seleccionado</span>
          </div>
        </div>
        <div className="mt-3 pt-3" style={{ borderTop: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: '#94a3b8' }}>Altura = PIB relativo</div>
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
