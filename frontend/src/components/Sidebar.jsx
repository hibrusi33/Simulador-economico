// Sidebar.jsx
import { useState, useEffect } from 'react';
import { LineChart, Line, AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const IDEOLOGIES = [
  {
    id: 'Capitalismo',
    icon: '💰',
    color: 'from-green-500 to-emerald-600',
    description: 'Economía de libre mercado con mínima intervención estatal. Prioriza crecimiento económico y libertad empresarial.'
  },
  {
    id: 'Capitalismo Neoliberal',
    icon: '🏦',
    color: 'from-blue-500 to-cyan-600',
    description: 'Libre mercado extremo con privatización masiva y desregulación. Máxima libertad económica, mínimo estado de bienestar.'
  },
  {
    id: 'Comunismo',
    icon: '🚩',
    color: 'from-red-600 to-rose-700',
    description: 'Economía planificada centralmente, propiedad colectiva de medios de producción. Control total del estado.'
  },
  {
    id: 'Socialismo',
    icon: '✊',
    color: 'from-red-400 to-pink-500',
    description: 'Estado controla sectores clave de la economía. Redistribución de riqueza y servicios públicos amplios.'
  },
  {
    id: 'Socialismo Democrático',
    icon: '🌹',
    color: 'from-pink-500 to-purple-600',
    description: 'Combina economía mixta con democracia plena. Estado de bienestar robusto con mercados regulados.'
  },
  {
    id: 'Teocracia',
    icon: '🕌',
    color: 'from-purple-600 to-indigo-700',
    description: 'Gobierno basado en principios religiosos. Economía y sociedad regidas por doctrina religiosa.'
  },
  {
    id: 'Autoritarismo',
    icon: '👁️',
    color: 'from-gray-700 to-gray-900',
    description: 'Poder concentrado en élite o líder. Control político estricto, economía dirigida según intereses del régimen.'
  },
  {
    id: 'Tecnocracia',
    icon: '⚙️',
    color: 'from-indigo-500 to-blue-600',
    description: 'Gobierno de expertos y científicos. Decisiones basadas en datos, eficiencia y optimización tecnológica.'
  },
  {
    id: 'Anarcocapitalismo',
    icon: '⚡',
    color: 'from-yellow-500 to-orange-600',
    description: 'Ausencia de estado, mercado completamente libre. Propiedad privada absoluta y contratos voluntarios.'
  },
  {
    id: 'Socialdemocracia',
    icon: '🤝',
    color: 'from-blue-400 to-indigo-500',
    description: 'Capitalismo regulado con fuerte protección social. Balance entre mercado libre y justicia social.'
  }
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
      <div className="w-full rounded-full h-2 overflow-hidden border" style={{ backgroundColor: 'var(--color-bg-dark)', borderColor: 'var(--color-border)' }}>
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
        <div className="border rounded-lg p-3 backdrop-blur-sm" style={{ backgroundColor: 'rgba(15, 23, 42, 0.95)', borderColor: 'var(--color-primary)' }}>
          <p className="font-bold mb-2" style={{ color: 'var(--color-primary)' }}>Mes {label}</p>
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
    <div className="w-full h-full overflow-y-auto" style={{ backgroundColor: 'var(--color-bg-dark)' }}>

      {/* Header */}
      <div className="p-6 border-b sticky top-0 z-10 backdrop-blur-sm" style={{ borderColor: 'var(--color-border)', backgroundColor: 'var(--color-bg-card)' }}>
        <h1 className="text-3xl font-bold mb-2 tracking-wider" style={{ color: 'var(--color-primary)' }}>
          SIMULADOR GEOPOLÍTICO
        </h1>
        <p className="text-sm" style={{ color: '#94a3b8' }}>
          {gamePhase === 'setup' ? '⚙️ Configuración' : `📊 Simulación - Mes ${currentMonth + 1}/50`}
        </p>
      </div>

      {/* ========== FASE SETUP ========== */}
      {gamePhase === 'setup' && (
        <div className="p-6 space-y-6">
          
          {/* Instrucciones */}
          <div className="border rounded-lg p-4 backdrop-blur-sm" style={{ backgroundColor: 'rgba(96, 165, 250, 0.1)', borderColor: 'var(--color-border)' }}>
            <h3 className="font-bold mb-2 flex items-center gap-2" style={{ color: 'var(--color-primary)' }}>
              <span>📍</span>
              <span>INSTRUCCIONES</span>
            </h3>
            <ol className="text-sm space-y-1 list-decimal list-inside" style={{ color: 'var(--color-text)' }}>
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
              <p className="text-lg font-semibold" style={{ color: '#94a3b8' }}>
                Selecciona un país en el globo
              </p>
              <p className="text-sm mt-2" style={{ color: '#64748b' }}>
                Haz clic en cualquier país disponible
              </p>
            </div>
          )}

          {/* Si hay países seleccionados */}
          {Object.keys(selectedCountries).length > 0 && (
            <div className="space-y-6">
              
              <div className="border rounded-lg p-4" style={{ backgroundColor: 'var(--color-bg-card)', borderColor: 'var(--color-border)' }}>
                <h3 className="font-bold mb-3 flex items-center justify-between" style={{ color: 'var(--color-primary)' }}>
                  <span>PAÍSES CONFIGURADOS ({Object.keys(selectedCountries).length})</span>
                </h3>
              </div>

              {/* Iterar sobre cada país seleccionado */}
              {Object.entries(selectedCountries).map(([countryCode, ideology]) => {
                const resources = countryResources[countryCode];
                
                return (
                  <div
                    key={countryCode}
                    className="border rounded-lg p-5 backdrop-blur-sm"
                    style={{ backgroundColor: 'var(--color-bg-card)', borderColor: 'var(--color-border)' }}
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
                      <div className="mb-4 border rounded-lg p-4" style={{ backgroundColor: 'rgba(15, 23, 42, 0.5)', borderColor: 'var(--color-border)' }}>
                        <h4 className="font-bold text-sm mb-3 flex items-center gap-2" style={{ color: 'var(--color-primary)' }}>
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
                        <div className="mt-3 pt-3 border-t" style={{ borderColor: 'var(--color-border)' }}>
                          <div className="flex items-center justify-between">
                            <span className="text-xs" style={{ color: '#94a3b8' }}>💵 PIB Inicial</span>
                            <span className="font-bold" style={{ color: 'var(--color-primary)' }}>${resources.pib_inicial}B</span>
                          </div>
                        </div>
                      </div>
                    )}

                    {/* Selector de Ideología */}
                    <div>
                      <h4 className="font-bold text-sm mb-3 flex items-center gap-2" style={{ color: 'var(--color-primary)' }}>
                        <span>🎯</span>
                        <span>IDEOLOGÍA ASIGNADA</span>
                      </h4>
                      <div className="grid grid-cols-2 gap-2">
                        {IDEOLOGIES.map((ideo) => {
                          const isSelected = ideology === ideo.id;
                          return (
                            <button
                              key={ideo.id}
                              title={ideo.description}
                              onClick={() => {
                                const newCountries = { ...selectedCountries };
                                newCountries[countryCode] = ideo.id;
                                onIdeologyChange(newCountries);
                              }}
                              className={`
                                px-3 py-2 rounded-lg text-xs font-bold transition-all duration-200
                                ${isSelected
                                  ? `bg-gradient-to-r ${ideo.color} text-white shadow-lg scale-105 border-2`
                                  : 'border hover:text-white'
                                }
                              `}
                              style={isSelected ? { borderColor: 'var(--color-primary)', boxShadow: '0 10px 15px -3px rgba(96, 165, 250, 0.3)' } : { backgroundColor: 'rgba(30, 41, 59, 0.5)', color: '#94a3b8', borderColor: 'var(--color-border)' }}
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
                className="w-full font-bold py-5 px-6 rounded-lg transition-all duration-300 transform hover:scale-105 disabled:transform-none shadow-2xl border disabled:cursor-not-allowed"
                style={isSimulating ?
                  { backgroundColor: '#64748b', color: 'white', borderColor: '#64748b' } :
                  { background: 'linear-gradient(to right, var(--color-primary), var(--color-secondary))', color: 'white', borderColor: 'var(--color-primary)', boxShadow: '0 25px 50px -12px rgba(96, 165, 250, 0.5)' }
                }
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
          <div className="border rounded-lg p-5 backdrop-blur-sm" style={{ background: 'linear-gradient(to right, rgba(96, 165, 250, 0.1), rgba(167, 139, 250, 0.1))', borderColor: 'var(--color-border)' }}>
            <div className="flex items-center justify-between mb-3">
              <div>
                <div className="font-bold text-2xl" style={{ color: 'var(--color-primary)' }}>MES {currentMonth + 1}</div>
                <div className="text-sm" style={{ color: '#94a3b8' }}>Año {Math.floor(currentMonth / 12) + 1}, Mes {(currentMonth % 12) + 1}</div>
              </div>
              <div className="text-right">
                <div className="text-white font-bold text-2xl">{Math.round((currentMonth + 1) / 50 * 100)}%</div>
                <div className="text-xs" style={{ color: '#94a3b8' }}>Completado</div>
              </div>
            </div>
            <div className="w-full rounded-full h-4 overflow-hidden border" style={{ backgroundColor: 'var(--color-bg-dark)', borderColor: 'var(--color-border)' }}>
              <div
                className="h-full transition-all duration-1000 relative"
                style={{ width: `${(currentMonth + 1) / 50 * 100}%`, background: 'linear-gradient(to right, var(--color-primary), var(--color-secondary), var(--color-accent))' }}
              >
                <div className="absolute inset-0 bg-white/20 animate-pulse"></div>
              </div>
            </div>
          </div>

          {/* Selector de país para detalle */}
          <div className="border rounded-lg p-4" style={{ backgroundColor: 'var(--color-bg-card)', borderColor: 'var(--color-border)' }}>
            <h4 className="font-bold text-sm mb-3" style={{ color: 'var(--color-primary)' }}>📌 ANÁLISIS DETALLADO</h4>
            <select
              value={selectedCountryForDetail || ''}
              onChange={(e) => onSelectCountryForDetail(e.target.value || null)}
              className="w-full border rounded px-3 py-2 text-sm text-white focus:outline-none transition-all"
              style={{ backgroundColor: 'var(--color-bg-dark)', borderColor: 'var(--color-border)' }}
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
          <div className="border rounded-lg p-5 backdrop-blur-sm" style={{ backgroundColor: 'var(--color-bg-card)', borderColor: 'var(--color-border)' }}>
            
            {/* Gráfica Comparativa (sin país seleccionado) - TOP 10 PAÍSES */}
            {!selectedCountryForDetail && (() => {
              // Calcular TOP 10 países por PIB actual (mes corriente)
              const top10Countries = Object.keys(simulationData || {})
                .map(code => ({
                  code,
                  pib: simulationData[code].proyeccion[currentMonth]?.PIB || 0
                }))
                .sort((a, b) => b.pib - a.pib)
                .slice(0, 10)
                .map(item => item.code);

              return (
                <div>
                  <h3 className="font-bold mb-4 flex items-center gap-2" style={{ color: 'var(--color-primary)' }}>
                    <span>📈</span>
                    <span>TOP 10 ECONOMÍAS - PIB</span>
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
                        wrapperStyle={{ fontSize: '10px', maxHeight: '80px', overflowY: 'auto' }}
                        iconType="line"
                      />
                      {top10Countries.map(countryCode => (
                        <Line
                          key={countryCode}
                          type="monotone"
                          dataKey={countryCode}
                          name={simulationData[countryCode].nombre}
                          stroke={countryColors[countryCode] || '#60a5fa'}
                          strokeWidth={2}
                          dot={false}
                          activeDot={{ r: 6 }}
                        />
                      ))}
                    </LineChart>
                  </ResponsiveContainer>
                </div>
              );
            })()}

            {/* Gráfica Detallada (país seleccionado) */}
            {selectedCountryForDetail && simulationData[selectedCountryForDetail] && (
              <div>
                <h3 className="font-bold mb-2 flex items-center gap-2" style={{ color: 'var(--color-primary)' }}>
                  <span>📊</span>
                  <span>{simulationData[selectedCountryForDetail].nombre}</span>
                </h3>
                <p className="text-xs mb-4" style={{ color: '#94a3b8' }}>
                  {simulationData[selectedCountryForDetail].ideologia}
                </p>
                
                {/* Gráfica de Área con doble eje Y */}
                <ResponsiveContainer width="100%" height={300}>
                  <AreaChart data={prepareDetailedData(selectedCountryForDetail)}>
                    <defs>
                      <linearGradient id="colorPIB" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#60a5fa" stopOpacity={0.8}/>
                        <stop offset="95%" stopColor="#60a5fa" stopOpacity={0}/>
                      </linearGradient>
                      <linearGradient id="colorBienestar" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#34d399" stopOpacity={0.8}/>
                        <stop offset="95%" stopColor="#34d399" stopOpacity={0}/>
                      </linearGradient>
                      <linearGradient id="colorLibertad" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#a78bfa" stopOpacity={0.8}/>
                        <stop offset="95%" stopColor="#a78bfa" stopOpacity={0}/>
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                    <XAxis
                      dataKey="mes"
                      stroke="#64748b"
                      style={{ fontSize: '12px' }}
                      label={{ value: 'Mes', position: 'insideBottom', offset: -5, fill: '#64748b' }}
                    />
                    {/* Eje izquierdo para PIB */}
                    <YAxis
                      yAxisId="left"
                      stroke="#60a5fa"
                      style={{ fontSize: '12px' }}
                      label={{ value: 'PIB (Miles M)', angle: -90, position: 'insideLeft', fill: '#60a5fa', style: { fontSize: '11px' } }}
                    />
                    {/* Eje derecho para Bienestar y Libertad */}
                    <YAxis
                      yAxisId="right"
                      orientation="right"
                      stroke="#34d399"
                      style={{ fontSize: '12px' }}
                      domain={[0, 100]}
                      label={{ value: 'Índices (0-100)', angle: 90, position: 'insideRight', fill: '#34d399', style: { fontSize: '11px' } }}
                    />
                    <Tooltip content={<CustomTooltip />} />
                    <Legend wrapperStyle={{ fontSize: '11px' }} />
                    <Area
                      yAxisId="left"
                      type="monotone"
                      dataKey="PIB"
                      stroke="#60a5fa"
                      fillOpacity={1}
                      fill="url(#colorPIB)"
                      name="PIB (Miles de Millones)"
                    />
                    <Area
                      yAxisId="right"
                      type="monotone"
                      dataKey="Bienestar"
                      stroke="#34d399"
                      fillOpacity={1}
                      fill="url(#colorBienestar)"
                      name="Bienestar (0-100)"
                    />
                    <Area
                      yAxisId="right"
                      type="monotone"
                      dataKey="Libertad"
                      stroke="#a78bfa"
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
                      <div className="border rounded p-3 text-center" style={{ backgroundColor: 'rgba(96, 165, 250, 0.1)', borderColor: '#60a5fa' }}>
                        <div className="text-xs mb-1" style={{ color: '#60a5fa' }}>PIB</div>
                        <div className="text-white font-bold text-lg">
                          ${simulationData[selectedCountryForDetail].proyeccion[currentMonth].PIB.toFixed(0)}B
                        </div>
                      </div>
                      <div className="border rounded p-3 text-center" style={{ backgroundColor: 'rgba(52, 211, 153, 0.1)', borderColor: '#34d399' }}>
                        <div className="text-xs mb-1" style={{ color: '#34d399' }}>Bienestar</div>
                        <div className="text-white font-bold text-lg">
                          {simulationData[selectedCountryForDetail].proyeccion[currentMonth].Bienestar.toFixed(0)}
                        </div>
                      </div>
                      <div className="border rounded p-3 text-center" style={{ backgroundColor: 'rgba(167, 139, 250, 0.1)', borderColor: '#a78bfa' }}>
                        <div className="text-xs mb-1" style={{ color: '#a78bfa' }}>Libertad</div>
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
            <div className="border rounded-lg p-6 text-center backdrop-blur-sm animate-pulse" style={{ background: 'linear-gradient(to right, rgba(52, 211, 153, 0.2), rgba(16, 185, 129, 0.2))', borderColor: '#34d399' }}>
              <div className="text-6xl mb-3">🎉</div>
              <div className="font-bold text-2xl mb-2" style={{ color: '#34d399' }}>SIMULACIÓN COMPLETADA</div>
              <div className="text-sm" style={{ color: 'var(--color-text)' }}>Los 50 meses han finalizado exitosamente</div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default Sidebar;
