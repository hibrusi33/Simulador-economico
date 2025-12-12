// Sidebar.jsx
import { useState, useEffect } from 'react';
import { LineChart, Line, AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const IDEOLOGIES = [
  { id: 'Capitalismo', icon: '💰', color: 'from-green-500 to-emerald-600' },
  { id: 'Capitalismo Neoliberal', icon: '🏦', color: 'from-blue-500 to-cyan-600' },
  { id: 'Comunismo', icon: '🚩', color: 'from-red-600 to-rose-700' },
  { id: 'Socialismo', icon: '✊', color: 'from-red-400 to-pink-500' },
  { id: 'Socialismo Democrático', icon: '🌹', color: 'from-pink-500 to-purple-600' },
  { id: 'Teocracia', icon: '🕌', color: 'from-purple-600 to-indigo-700' },
  { id: 'Autoritarismo', icon: '👁️', color: 'from-gray-700 to-gray-900' },
  { id: 'Tecnocracia', icon: '⚙️', color: 'from-indigo-500 to-blue-600' },
  { id: 'Anarcocapitalismo', icon: '⚡', color: 'from-yellow-500 to-orange-600' },
  { id: 'Socialdemocracia', icon: '🤝', color: 'from-blue-400 to-indigo-500' }
];

const Sidebar = ({ 
  gamePhase, 
  selectedCountries, 
  onIdeologyChange, 
  onStartSimulation, 
  isSimulating,
  simulationData,
  currentMonth,
  selectedCountryForDetail = null,
  onSelectCountryForDetail
}) => {
  const [countryResources, setCountryResources] = useState({});
  const [loadingResources, setLoadingResources] = useState(false);

  // Cargar recursos de países seleccionados
  useEffect(() => {
    const fetchResources = async () => {
      if (Object.keys(selectedCountries).length === 0) return;

      setLoadingResources(true);
      const resources = {};

      for (const countryCode of Object.keys(selectedCountries)) {
        try {
          const response = await fetch(`http://localhost:8000/atlas/${countryCode}`);
          if (response.ok) {
            const data = await response.json();
            resources[countryCode] = data.datos;
          }
        } catch (error) {
          console.error(`Error cargando recursos de ${countryCode}:`, error);
        }
      }

      setCountryResources(resources);
      setLoadingResources(false);
    };

    fetchResources();
  }, [selectedCountries]);

  // Obtener color según el valor del recurso
  const getResourceColor = (value) => {
    if (value >= 0.7) return 'text-green-400';
    if (value >= 0.4) return 'text-yellow-400';
    return 'text-red-400';
  };

  // Obtener color de fondo según el valor
  const getResourceBgColor = (value) => {
    if (value >= 0.7) return 'bg-green-500/20';
    if (value >= 0.4) return 'bg-yellow-500/20';
    return 'bg-red-500/20';
  };

  // Renderizar barra de progreso de recurso
  const ResourceBar = ({ label, value, icon }) => (
    <div className="mb-3">
      <div className="flex items-center justify-between mb-1">
        <span className="text-xs text-gray-400 flex items-center gap-1">
          <span>{icon}</span>
          {label}
        </span>
        <span className={`text-xs font-bold ${getResourceColor(value)}`}>
          {(value * 100).toFixed(0)}%
        </span>
      </div>
      <div className="w-full bg-gray-800 rounded-full h-2 overflow-hidden border border-cyan-400/20">
        <div 
          className={`h-full transition-all duration-500 ${
            value >= 0.7 ? 'bg-gradient-to-r from-green-500 to-emerald-400' :
            value >= 0.4 ? 'bg-gradient-to-r from-yellow-500 to-orange-400' :
            'bg-gradient-to-r from-red-500 to-rose-400'
          }`}
          style={{ width: `${value * 100}%` }}
        />
      </div>
    </div>
  );

  // Preparar datos para gráfica comparativa (todos los países)
  const prepareComparativeData = () => {
    if (!simulationData) return [];
    
    const data = [];
    for (let month = 0; month <= currentMonth; month++) {
      const monthData = { mes: month + 1 };
      
      Object.keys(simulationData).forEach(countryCode => {
        const country = simulationData[countryCode];
        if (country.proyeccion && country.proyeccion[month]) {
          monthData[countryCode] = country.proyeccion[month].PIB;
        }
      });
      
      data.push(monthData);
    }
    
    return data;
  };

  // Preparar datos para gráfica detallada de un país
  const prepareDetailedData = (countryCode) => {
    if (!simulationData || !simulationData[countryCode]) return [];
    
    const country = simulationData[countryCode];
    const data = [];
    
    for (let month = 0; month <= currentMonth; month++) {
      if (country.proyeccion && country.proyeccion[month]) {
        data.push({
          mes: month + 1,
          PIB: country.proyeccion[month].PIB,
          Bienestar: country.proyeccion[month].Bienestar,
          Libertad: country.proyeccion[month].Libertad
        });
      }
    }
    
    return data;
  };

  // Colores para países en gráfica comparativa
  const countryColors = {
    'USA': '#3b82f6',
    'China': '#ef4444',
    'Russia': '#8b5cf6',
    'Germany': '#000000',
    'Japan': '#dc2626',
    'Spain': '#fbbf24',
    'India': '#f97316',
    'Brazil': '#22c55e',
    'SaudiArabia': '#14b8a6',
    'France': '#6366f1',
    'UK': '#ec4899',
    'Mexico': '#84cc16',
    'SouthKorea': '#06b6d4',
    'Australia': '#fbbf24',
    'Canada': '#f43f5e'
  };

  // Custom Tooltip para las gráficas
  const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-black/90 border border-cyan-400/50 rounded-lg p-3 backdrop-blur-sm">
          <p className="text-cyan-400 font-bold mb-2">Mes {label}</p>
          {payload.map((entry, index) => (
            <p key={index} style={{ color: entry.color }} className="text-sm">
              {entry.name}: {typeof entry.value === 'number' ? entry.value.toFixed(2) : entry.value}
            </p>
          ))}
        </div>
      );
    }
    return null;
  };

  return (
    <div className="w-full h-full bg-gradient-to-br from-gray-900 via-black to-gray-900 overflow-y-auto">
      
      {/* Header */}
      <div className="p-6 border-b border-cyan-400/30 bg-black/40 sticky top-0 z-10 backdrop-blur-sm">
        <h1 className="text-3xl font-bold text-cyan-400 mb-2 tracking-wider">
          SIMULADOR GEOPOLÍTICO
        </h1>
        <p className="text-gray-400 text-sm">
          {gamePhase === 'setup' ? '⚙️ Configuración' : `📊 Simulación - Mes ${currentMonth + 1}/50`}
        </p>
      </div>

      {/* ========== FASE SETUP ========== */}
      {gamePhase === 'setup' && (
        <div className="p-6 space-y-6">
          
          {/* Instrucciones */}
          <div className="bg-cyan-500/10 border border-cyan-400/30 rounded-lg p-4 backdrop-blur-sm">
            <h3 className="text-cyan-400 font-bold mb-2 flex items-center gap-2">
              <span>📍</span>
              <span>INSTRUCCIONES</span>
            </h3>
            <ol className="text-sm text-gray-300 space-y-1 list-decimal list-inside">
              <li>Haz clic en países del globo para seleccionarlos</li>
              <li>Asigna una ideología a cada país</li>
              <li>Presiona "INICIAR SIMULACIÓN"</li>
              <li>Observa la evolución económica en 50 meses</li>
            </ol>
          </div>

          {/* Si no hay países seleccionados */}
          {Object.keys(selectedCountries).length === 0 && (
            <div className="text-center py-12">
              <div className="text-6xl mb-4 animate-pulse">🌍</div>
              <p className="text-gray-400 text-lg font-semibold">
                Selecciona un país en el globo
              </p>
              <p className="text-gray-600 text-sm mt-2">
                Haz clic en cualquier país disponible
              </p>
            </div>
          )}

          {/* Si hay países seleccionados */}
          {Object.keys(selectedCountries).length > 0 && (
            <div className="space-y-6">
              
              <div className="bg-black/40 border border-cyan-400/20 rounded-lg p-4">
                <h3 className="text-cyan-400 font-bold mb-3 flex items-center justify-between">
                  <span>PAÍSES CONFIGURADOS ({Object.keys(selectedCountries).length})</span>
                </h3>
              </div>

              {/* Iterar sobre cada país seleccionado */}
              {Object.entries(selectedCountries).map(([countryCode, ideology]) => {
                const resources = countryResources[countryCode];
                
                return (
                  <div 
                    key={countryCode}
                    className="bg-gradient-to-br from-gray-800/50 to-gray-900/50 border border-cyan-400/20 rounded-lg p-5 backdrop-blur-sm"
                  >
                    {/* Nombre del país */}
                    <div className="flex items-center justify-between mb-4">
                      <h2 className="text-2xl font-bold text-white">
                        {resources?.nombre || countryCode}
                      </h2>
                      <button
                        onClick={() => {
                          const newCountries = { ...selectedCountries };
                          delete newCountries[countryCode];
                          onIdeologyChange(newCountries);
                        }}
                        className="text-red-400 hover:text-red-300 text-xs bg-red-500/20 px-3 py-1 rounded border border-red-500/30 transition-all"
                      >
                        ✕ Eliminar
                      </button>
                    </div>

                    {/* Panel de Recursos */}
                    {resources && (
                      <div className="mb-4 bg-black/30 border border-cyan-400/10 rounded-lg p-4">
                        <h4 className="text-cyan-400 font-bold text-sm mb-3 flex items-center gap-2">
                          <span>📊</span>
                          <span>RECURSOS NACIONALES</span>
                        </h4>
                        <div className="grid grid-cols-2 gap-3">
                          <div className="col-span-2">
                            <ResourceBar 
                              label="Recursos Fósiles" 
                              value={resources.recursos_fosiles} 
                              icon="⛽"
                            />
                          </div>
                          <div className="col-span-2">
                            <ResourceBar 
                              label="Potencial Renovable" 
                              value={resources.potencial_renovable} 
                              icon="♻️"
                            />
                          </div>
                          <div className="col-span-2">
                            <ResourceBar 
                              label="Tecnología" 
                              value={resources.tecnologia} 
                              icon="💻"
                            />
                          </div>
                          <div className="col-span-2">
                            <ResourceBar 
                              label="Capital Humano" 
                              value={resources.capital_humano} 
                              icon="👥"
                            />
                          </div>
                          <ResourceBar 
                            label="Tierra Arable" 
                            value={resources.tierra_arable} 
                            icon="🌾"
                          />
                          <ResourceBar 
                            label="Acceso Marítimo" 
                            value={resources.acceso_maritimo} 
                            icon="🌊"
                          />
                        </div>
                        
                        {/* PIB Inicial */}
                        <div className="mt-3 pt-3 border-t border-cyan-400/20">
                          <div className="flex items-center justify-between">
                            <span className="text-gray-400 text-xs">💵 PIB Inicial</span>
                            <span className="text-cyan-400 font-bold">${resources.pib_inicial}B</span>
                          </div>
                        </div>
                      </div>
                    )}

                    {/* Selector de Ideología */}
                    <div>
                      <h4 className="text-cyan-400 font-bold text-sm mb-3 flex items-center gap-2">
                        <span>🎯</span>
                        <span>IDEOLOGÍA ASIGNADA</span>
                      </h4>
                      <div className="grid grid-cols-2 gap-2">
                        {IDEOLOGIES.map((ideo) => {
                          const isSelected = ideology === ideo.id;
                          return (
                            <button
                              key={ideo.id}
                              onClick={() => {
                                const newCountries = { ...selectedCountries };
                                newCountries[countryCode] = ideo.id;
                                onIdeologyChange(newCountries);
                              }}
                              className={`
                                px-3 py-2 rounded-lg text-xs font-bold transition-all duration-200
                                ${isSelected 
                                  ? `bg-gradient-to-r ${ideo.color} text-white shadow-lg shadow-cyan-500/30 scale-105 border-2 border-cyan-400`
                                  : 'bg-gray-800/50 text-gray-400 border border-gray-700 hover:bg-gray-700/50 hover:text-white'
                                }
                              `}
                            >
                              <div>{ideo.icon}</div>
                              <div className="text-[10px] mt-1">{ideo.id}</div>
                            </button>
                          );
                        })}
                      </div>
                    </div>
                  </div>
                );
              })}

              {/* Botón INICIAR SIMULACIÓN */}
              <button
                onClick={onStartSimulation}
                disabled={isSimulating}
                className="w-full bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-400 hover:to-blue-400 disabled:from-gray-600 disabled:to-gray-700 disabled:cursor-not-allowed text-white font-bold py-5 px-6 rounded-lg transition-all duration-300 transform hover:scale-105 disabled:transform-none shadow-2xl shadow-cyan-500/50 border border-cyan-400/50"
              >
                {isSimulating ? (
                  <span className="flex items-center justify-center gap-3">
                    <svg className="animate-spin h-6 w-6" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                    </svg>
                    <span className="text-lg">GENERANDO SIMULACIÓN CON IA...</span>
                  </span>
                ) : (
                  <span className="flex items-center justify-center gap-2 text-lg">
                    <span>🚀</span>
                    <span>INICIAR SIMULACIÓN DE 50 MESES</span>
                  </span>
                )}
              </button>
            </div>
          )}
        </div>
      )}

      {/* ========== FASE RUNNING ========== */}
      {gamePhase === 'running' && (
        <div className="p-6 space-y-6">
          
          {/* Progreso Temporal */}
          <div className="bg-gradient-to-r from-cyan-500/10 to-blue-500/10 border border-cyan-400/30 rounded-lg p-5 backdrop-blur-sm">
            <div className="flex items-center justify-between mb-3">
              <div>
                <div className="text-cyan-400 font-bold text-2xl">MES {currentMonth + 1}</div>
                <div className="text-gray-400 text-sm">Año {Math.floor(currentMonth / 12) + 1}, Mes {(currentMonth % 12) + 1}</div>
              </div>
              <div className="text-right">
                <div className="text-white font-bold text-2xl">{Math.round((currentMonth + 1) / 50 * 100)}%</div>
                <div className="text-gray-400 text-xs">Completado</div>
              </div>
            </div>
            <div className="w-full bg-gray-800 rounded-full h-4 overflow-hidden border border-cyan-400/30">
              <div 
                className="bg-gradient-to-r from-cyan-500 via-blue-500 to-purple-500 h-full transition-all duration-1000 relative"
                style={{ width: `${(currentMonth + 1) / 50 * 100}%` }}
              >
                <div className="absolute inset-0 bg-white/20 animate-pulse"></div>
              </div>
            </div>
          </div>

          {/* Selector de país para detalle */}
          <div className="bg-black/40 border border-cyan-400/20 rounded-lg p-4">
            <h4 className="text-cyan-400 font-bold text-sm mb-3">📌 ANÁLISIS DETALLADO</h4>
            <select
              value={selectedCountryForDetail || ''}
              onChange={(e) => onSelectCountryForDetail(e.target.value || null)}
              className="w-full bg-gray-900 border border-cyan-400/30 rounded px-3 py-2 text-sm text-white focus:outline-none focus:border-cyan-400 transition-all"
            >
              <option value="">Comparativa Global (Todos)</option>
              {Object.keys(simulationData || {}).map(code => (
                <option key={code} value={code}>
                  {simulationData[code].nombre} ({simulationData[code].ideologia})
                </option>
              ))}
            </select>
          </div>

          {/* Gráficas */}
          <div className="bg-gradient-to-br from-gray-800/50 to-gray-900/50 border border-cyan-400/20 rounded-lg p-5 backdrop-blur-sm">
            
            {/* Gráfica Comparativa (sin país seleccionado) */}
            {!selectedCountryForDetail && (
              <div>
                <h3 className="text-cyan-400 font-bold mb-4 flex items-center gap-2">
                  <span>📈</span>
                  <span>COMPARATIVA MUNDIAL - PIB</span>
                </h3>
                <ResponsiveContainer width="100%" height={300}>
                  <LineChart data={prepareComparativeData()}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                    <XAxis 
                      dataKey="mes" 
                      stroke="#64748b"
                      style={{ fontSize: '12px' }}
                      label={{ value: 'Mes', position: 'insideBottom', offset: -5, fill: '#64748b' }}
                    />
                    <YAxis 
                      stroke="#64748b"
                      style={{ fontSize: '12px' }}
                      label={{ value: 'PIB (Miles de Millones)', angle: -90, position: 'insideLeft', fill: '#64748b' }}
                    />
                    <Tooltip content={<CustomTooltip />} />
                    <Legend 
                      wrapperStyle={{ fontSize: '11px' }}
                      iconType="line"
                    />
                    {Object.keys(simulationData || {}).map(countryCode => (
                      <Line
                        key={countryCode}
                        type="monotone"
                        dataKey={countryCode}
                        name={simulationData[countryCode].nombre}
                        stroke={countryColors[countryCode] || '#00ffff'}
                        strokeWidth={2}
                        dot={false}
                        activeDot={{ r: 6 }}
                      />
                    ))}
                  </LineChart>
                </ResponsiveContainer>
              </div>
            )}

            {/* Gráfica Detallada (país seleccionado) */}
            {selectedCountryForDetail && simulationData[selectedCountryForDetail] && (
              <div>
                <h3 className="text-cyan-400 font-bold mb-2 flex items-center gap-2">
                  <span>📊</span>
                  <span>{simulationData[selectedCountryForDetail].nombre}</span>
                </h3>
                <p className="text-gray-400 text-xs mb-4">
                  {simulationData[selectedCountryForDetail].ideologia}
                </p>
                
                {/* Gráfica de Área */}
                <ResponsiveContainer width="100%" height={300}>
                  <AreaChart data={prepareDetailedData(selectedCountryForDetail)}>
                    <defs>
                      <linearGradient id="colorPIB" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#00ffff" stopOpacity={0.8}/>
                        <stop offset="95%" stopColor="#00ffff" stopOpacity={0}/>
                      </linearGradient>
                      <linearGradient id="colorBienestar" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#22c55e" stopOpacity={0.8}/>
                        <stop offset="95%" stopColor="#22c55e" stopOpacity={0}/>
                      </linearGradient>
                      <linearGradient id="colorLibertad" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#f59e0b" stopOpacity={0.8}/>
                        <stop offset="95%" stopColor="#f59e0b" stopOpacity={0}/>
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                    <XAxis 
                      dataKey="mes" 
                      stroke="#64748b"
                      style={{ fontSize: '12px' }}
                      label={{ value: 'Mes', position: 'insideBottom', offset: -5, fill: '#64748b' }}
                    />
                    <YAxis 
                      stroke="#64748b"
                      style={{ fontSize: '12px' }}
                    />
                    <Tooltip content={<CustomTooltip />} />
                    <Legend wrapperStyle={{ fontSize: '11px' }} />
                    <Area 
                      type="monotone" 
                      dataKey="PIB" 
                      stroke="#00ffff" 
                      fillOpacity={1} 
                      fill="url(#colorPIB)"
                      name="PIB (Miles de Millones)"
                    />
                    <Area 
                      type="monotone" 
                      dataKey="Bienestar" 
                      stroke="#22c55e" 
                      fillOpacity={1} 
                      fill="url(#colorBienestar)"
                      name="Bienestar (0-100)"
                    />
                    <Area 
                      type="monotone" 
                      dataKey="Libertad" 
                      stroke="#f59e0b" 
                      fillOpacity={1} 
                      fill="url(#colorLibertad)"
                      name="Libertad (0-100)"
                    />
                  </AreaChart>
                </ResponsiveContainer>

                {/* Estadísticas actuales del país */}
                <div className="grid grid-cols-3 gap-3 mt-5">
                  {simulationData[selectedCountryForDetail].proyeccion[currentMonth] && (
                    <>
                      <div className="bg-cyan-500/10 border border-cyan-400/30 rounded p-3 text-center">
                        <div className="text-cyan-400 text-xs mb-1">PIB</div>
                        <div className="text-white font-bold text-lg">
                          ${simulationData[selectedCountryForDetail].proyeccion[currentMonth].PIB.toFixed(0)}B
                        </div>
                      </div>
                      <div className="bg-green-500/10 border border-green-400/30 rounded p-3 text-center">
                        <div className="text-green-400 text-xs mb-1">Bienestar</div>
                        <div className="text-white font-bold text-lg">
                          {simulationData[selectedCountryForDetail].proyeccion[currentMonth].Bienestar.toFixed(0)}
                        </div>
                      </div>
                      <div className="bg-orange-500/10 border border-orange-400/30 rounded p-3 text-center">
                        <div className="text-orange-400 text-xs mb-1">Libertad</div>
                        <div className="text-white font-bold text-lg">
                          {simulationData[selectedCountryForDetail].proyeccion[currentMonth].Libertad.toFixed(0)}
                        </div>
                      </div>
                    </>
                  )}
                </div>
              </div>
            )}
          </div>

          {/* Mensaje de fin de simulación */}
          {currentMonth === 49 && (
            <div className="bg-gradient-to-r from-green-500/20 to-emerald-500/20 border border-green-400 rounded-lg p-6 text-center backdrop-blur-sm animate-pulse">
              <div className="text-6xl mb-3">🎉</div>
              <div className="text-green-400 font-bold text-2xl mb-2">SIMULACIÓN COMPLETADA</div>
              <div className="text-gray-300 text-sm">Los 50 meses han finalizado exitosamente</div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default Sidebar;
