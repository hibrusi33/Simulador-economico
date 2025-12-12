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
    'CAN': 'Canada'
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
    
    // País seleccionado: borde cyan brillante
    if (selectedCountries.includes(countryCode)) {
      return '#00ffff';
    }

    // Hover effect
    if (hoverD && d === hoverD) {
      return '#00ccff';
    }
    
    if (!countryCode || !currentMonthData[countryCode]) {
      // Países no simulados: gris oscuro
      return 'rgba(50, 50, 70, 0.7)';
    }

    const data = currentMonthData[countryCode];
    const bienestar = data.Bienestar || 50;
    
    // Interpolación de color: Rojo (0) -> Amarillo (50) -> Verde (100)
    let color;
    if (bienestar < 50) {
      // Rojo a Amarillo
      const t = bienestar / 50;
      color = d3.interpolateRgb('#ff0000', '#ffff00')(t);
    } else {
      // Amarillo a Verde
      const t = (bienestar - 50) / 50;
      color = d3.interpolateRgb('#ffff00', '#00ff00')(t);
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
    
    return `<div style="color: white; background: rgba(0,0,0,0.9); padding: 10px; border-radius: 6px; font-family: monospace; border: 2px solid #00ffff;">
      <div style="font-size: 14px; font-weight: bold; color: #00ffff; margin-bottom: 4px;">${countryName}</div>
      <div style="font-size: 11px; color: #aaa; margin-bottom: 6px;">${data.ideologia || 'N/A'}</div>
      <div style="font-size: 12px;">
        <div style="color: #0ff;">PIB: $${data.PIB?.toFixed(0)} B (${pibChange > 0 ? '+' : ''}${pibChange}%)</div>
        <div style="color: ${data.Bienestar > 60 ? '#0f0' : data.Bienestar > 40 ? '#ff0' : '#f00'};">
          Bienestar: ${data.Bienestar?.toFixed(0)}/100
        </div>
        <div style="color: ${data.Libertad > 60 ? '#0f0' : data.Libertad > 40 ? '#ff0' : '#f00'};">
          Libertad: ${data.Libertad?.toFixed(0)}/100
        </div>
      </div>
    </div>`;
  };

  return (
    <div className="relative w-full h-full bg-black">
      <Globe
        ref={globeEl}
        
        // Datos
        polygonsData={countries.features}
        
        // Apariencia del globo
        globeImageUrl="//unpkg.com/three-globe/example/img/earth-night.jpg"
        backgroundImageUrl="//unpkg.com/three-globe/example/img/night-sky.png"
        
        // Atmósfera cyberpunk
        atmosphereColor="#00ffff"
        atmosphereAltitude={0.15}
        
        // Configuración de polígonos (países)
        polygonAltitude={getPolygonAltitude}
        polygonCapColor={getPolygonColor}
        polygonSideColor={() => 'rgba(0, 100, 150, 0.4)'}
        polygonStrokeColor={() => '#001122'}
        polygonLabel={getPolygonLabel}
        
        // Animación suave entre meses
        polygonsTransitionDuration={1000}
        
        // Interactividad
        onPolygonClick={handleCountryClick}
        onPolygonHover={setHoverD}
        
        // Controles
        enablePointerInteraction={true}
      />
      
      {/* Leyenda de colores */}
      <div className="absolute bottom-6 right-6 bg-black/80 border border-cyan-400 rounded-lg p-4 text-white font-mono text-sm backdrop-blur-sm">
        <div className="font-bold text-cyan-400 mb-2">LEYENDA</div>
        <div className="space-y-1">
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-green-500"></div>
            <span>Alto Bienestar (80-100)</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-yellow-400"></div>
            <span>Medio Bienestar (40-80)</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-red-500"></div>
            <span>Bajo Bienestar (0-40)</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 bg-cyan-400"></div>
            <span>País Seleccionado</span>
          </div>
        </div>
        <div className="mt-3 pt-3 border-t border-cyan-400/30">
          <div className="text-xs text-gray-400">Altura = PIB relativo</div>
        </div>
      </div>

      {/* Indicador de carga */}
      {countries.features.length === 0 && (
        <div className="absolute inset-0 flex items-center justify-center bg-black/70">
          <div className="text-cyan-400 font-mono text-xl animate-pulse">
            CARGANDO MAPA DEL MUNDO...
          </div>
        </div>
      )}
    </div>
  );
};

export default GlobeSelector;
