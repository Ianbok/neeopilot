import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import HomeScreen from './components/HomeScreen';

function App() {
  const [isSystemReady, setIsSystemReady] = useState(false);

  useEffect(() => {
    const initTimer = setTimeout(() => {
      setIsSystemReady(true);
    }, 1500);

    return () => clearTimeout(initTimer);
  }, []);

  if (!isSystemReady) {
    return (
      <div className="min-h-screen flex items-center justify-center" style={{ backgroundColor: 'var(--bg-secondary)' }}>
        <div className="text-center">
          <div className="mb-8">
            <div className="w-20 h-20 mx-auto rounded-2xl glass-effect flex items-center justify-center mb-4" style={{ backgroundColor: 'var(--bg-glass)' }}>
              <div className="w-12 h-12 bg-gradient-to-br from-cyan-400 to-green-400 rounded-xl flex items-center justify-center">
                <span className="text-xl font-bold text-white">N</span>
              </div>
            </div>
            <h1 className="text-3xl font-bold text-white mb-2">NeeOPiloT</h1>
            <p className="text-cyan-400">Automotive Interface System</p>
          </div>

          <div className="w-64 h-2 bg-gray-800 rounded-full overflow-hidden mx-auto">
            <div className="h-full bg-gradient-to-r from-cyan-400 to-green-400 rounded-full animate-pulse"></div>
          </div>
          <p className="text-white/60 mt-4 text-sm">Initializing systems...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex flex-col" style={{ backgroundColor: 'var(--bg-secondary)' }}>
      <Navbar />
      
      <main className="flex-1 relative">
        <HomeScreen />
      </main>

      <div className="fixed inset-0 pointer-events-none -z-20">
        <div className="absolute inset-0 bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900"></div>
        <div className="absolute top-0 left-0 w-full h-full bg-[radial-gradient(ellipse_at_top_left,_var(--neon-cyan)_0%,_transparent_50%)] opacity-10"></div>
        <div className="absolute bottom-0 right-0 w-full h-full bg-[radial-gradient(ellipse_at_bottom_right,_var(--neon-green)_0%,_transparent_50%)] opacity-10"></div>
      </div>
    </div>
  );
}

export default App;