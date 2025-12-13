// App.jsx
import { useState, useEffect, useRef } from 'react';
import GlobeSelector from './components/GlobeSelector';
import Sidebar from './components/Sidebar';

function App() {
  // Estado global de la aplicación
  const [gamePhase, setGamePhase] = useState('setup'); // 'setup' o 'running'
  const [selectedCountries, setSelectedCountries] = useState({}); // {countryCode: ideology}
  const [simulationData, setSimulationData] = useState(null);
  const [currentMonth, setCurrentMonth] = useState(0);
  const [isSimulating, setIsSimulating] = useState(false);
  const [currentMonthData, setCurrentMonthData] = useState({});
  const [errorMessage, setErrorMessage] = useState('');
  const [selectedCountryForDetail, setSelectedCountryForDetail] = useState(null); // Para gráfica detallada
  
  const simulationInterval = useRef(null);

  // Manejar selección de país desde el globo
  const handleSelectCountry = (countryCode, countryName) => {
    if (gamePhase === 'running') return; // No permitir cambios durante simulación

    // Si ya está seleccionado, removerlo
    if (selectedCountries[countryCode]) {
      const newSelected = { ...selectedCountries };
      delete newSelected[countryCode];
      setSelectedCountries(newSelected);
    } else {
      // Añadir con ideología por defecto
      setSelectedCountries({
        ...selectedCountries,
        [countryCode]: 'Capitalismo'
      });
    }
  };

  // Cambiar configuración completa de países (usado por Sidebar)
  const handleIdeologyChange = (newSelectedCountries) => {
    setSelectedCountries(newSelectedCountries);
  };

  // Iniciar simulación
  const startSimulation = async () => {
    if (Object.keys(selectedCountries).length === 0) {
      setErrorMessage('⚠️ Selecciona al menos un país');
      setTimeout(() => setErrorMessage(''), 3000);
      return;
    }

    setIsSimulating(true);
    setErrorMessage('');

    try {
      const response = await fetch('http://localhost:8000/simular_mundo', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          configuracion: selectedCountries
        })
      });

      if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`);
      }

      const data = await response.json();
      
      if (data.exito && data.resultados) {
        setSimulationData(data.resultados);
        setGamePhase('running');
        setCurrentMonth(0);
        setSelectedCountryForDetail(null); // Reset selección
        
        // Inicializar datos del primer mes
        updateCurrentMonthData(data.resultados, 0);
      } else {
        throw new Error('Formato de respuesta inválido');
      }
      
    } catch (error) {
      console.error('Error en simulación:', error);
      setErrorMessage(`❌ Error: ${error.message}. Verifica que el backend esté corriendo en puerto 8000.`);
    } finally {
      setIsSimulating(false);
    }
  };

  // Actualizar datos del mes actual
  const updateCurrentMonthData = (data, month) => {
    const monthData = {};
    
    Object.keys(data).forEach(countryCode => {
      const country = data[countryCode];
      if (country.proyeccion && country.proyeccion[month]) {
        monthData[countryCode] = {
          ...country.proyeccion[month],
          ideologia: country.ideologia,
          nombre: country.nombre,
          pib_inicial: country.recursos?.pib_inicial || 1000
        };
      }
    });
    
    setCurrentMonthData(monthData);
  };

  // Avanzar simulación automáticamente
  useEffect(() => {
    if (gamePhase === 'running' && simulationData && currentMonth < 50) {
      simulationInterval.current = setInterval(() => {
        setCurrentMonth(prev => {
          const nextMonth = prev + 1;
          if (nextMonth >= 50) {
            clearInterval(simulationInterval.current);
            return 49;
          }
          updateCurrentMonthData(simulationData, nextMonth);
          return nextMonth;
        });
      }, 1200); // Avanzar cada 1.2 segundos

      return () => {
        if (simulationInterval.current) {
          clearInterval(simulationInterval.current);
        }
      };
    }
  }, [gamePhase, simulationData, currentMonth]);

  // Reiniciar simulación
  const resetSimulation = () => {
    setGamePhase('setup');
    setSimulationData(null);
    setCurrentMonth(0);
    setCurrentMonthData({});
    setSelectedCountries({});
    setSelectedCountryForDetail(null);
    setErrorMessage('');
    if (simulationInterval.current) {
      clearInterval(simulationInterval.current);
    }
  };

  // Pausar/Reanudar
  const togglePause = () => {
    if (simulationInterval.current) {
      clearInterval(simulationInterval.current);
      simulationInterval.current = null;
    } else {
      // Reanudar
      setGamePhase('running');
    }
  };

  return (
    <div className="w-screen h-screen font-mono overflow-hidden" style={{ backgroundColor: 'var(--color-bg-dark)', color: 'var(--color-text)' }}>

      {/* Mensaje de Error Global (si existe) */}
      {errorMessage && (
        <div className="absolute top-4 left-1/2 transform -translate-x-1/2 z-50 bg-red-500/90 border border-red-400 rounded-lg px-6 py-3 shadow-2xl animate-pulse">
          <p className="text-white font-bold">{errorMessage}</p>
        </div>
      )}

      {/* Layout Principal: Responsive */}
      <div className="w-full h-full flex flex-col lg:flex-row">

        {/* Sidebar - Componente separado */}
        <div className="w-full lg:w-1/3 h-1/2 lg:h-full border-b lg:border-r" style={{ borderColor: 'var(--color-border)' }}>
          <Sidebar
            gamePhase={gamePhase}
            selectedCountries={selectedCountries}
            onIdeologyChange={handleIdeologyChange}
            onStartSimulation={startSimulation}
            isSimulating={isSimulating}
            simulationData={simulationData}
            currentMonth={currentMonth}
            selectedCountryForDetail={selectedCountryForDetail}
            onSelectCountryForDetail={setSelectedCountryForDetail}
          />
        </div>

        {/* Globo Derecha */}
        <div className="w-full lg:w-2/3 h-1/2 lg:h-full relative">
          <GlobeSelector
            onSelectCountry={handleSelectCountry}
            currentMonthData={currentMonthData}
            selectedCountries={Object.keys(selectedCountries)}
            isSimulationRunning={gamePhase === 'running'}
          />

          {/* Overlay de título cuando está en setup */}
          {gamePhase === 'setup' && (
            <div className="absolute top-6 left-6 rounded-lg p-4 backdrop-blur-sm" style={{ backgroundColor: 'var(--color-bg-card)', border: '1px solid var(--color-border)' }}>
              <div className="font-bold text-sm" style={{ color: 'var(--color-primary)' }}>🌍 SELECCIONA PAÍSES</div>
              <div className="text-xs mt-1" style={{ color: 'var(--color-text)', opacity: 0.7 }}>Haz clic en el globo</div>
            </div>
          )}

          {/* Controles de Simulación (solo en running) */}
          {gamePhase === 'running' && (
            <div className="absolute bottom-6 left-6 flex gap-3">
              <button
                onClick={togglePause}
                className="font-bold py-3 px-6 rounded-lg transition-all shadow-lg"
                style={{ backgroundColor: '#facc15', color: 'var(--color-bg-dark)' }}
              >
                {simulationInterval.current ? '⏸️ PAUSAR' : '▶️ REANUDAR'}
              </button>

              <button
                onClick={resetSimulation}
                className="font-bold py-3 px-6 rounded-lg transition-all shadow-lg"
                style={{ backgroundColor: '#ef4444', color: 'white' }}
              >
                🔄 REINICIAR
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
