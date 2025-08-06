import React, { useState, useEffect } from 'react';
import { Wifi, WifiOff, Bluetooth, BluetoothConnected, Moon, Sun, Battery, Signal } from 'lucide-react';

const Navbar = () => {
  const [currentTime, setCurrentTime] = useState(new Date());
  const [isDarkMode, setIsDarkMode] = useState(true);
  const [connectionStatus, setConnectionStatus] = useState({
    wifi: true,
    bluetooth: true,
    signal: 4
  });

  // Update time every second
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  // Format time for display
  const formatTime = (date) => {
    return date.toLocaleTimeString('en-US', {
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      hour12: false
    });
  };

  const formatDate = (date) => {
    return date.toLocaleDateString('en-US', {
      weekday: 'short',
      month: 'short',
      day: 'numeric'
    });
  };

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
  };

  const toggleConnection = (type) => {
    setConnectionStatus(prev => ({
      ...prev,
      [type]: !prev[type]
    }));
  };

  return (
    <nav className="w-full h-16 glass-effect touch-scale" style={{ backgroundColor: 'var(--bg-primary)' }}>
      <div className="flex items-center justify-between h-full px-6">
        
        {/* Left Section - Time & Date */}
        <div className="flex items-center space-x-4">
          <div className="text-center">
            <div className="text-2xl font-bold text-cyan-400 font-mono tracking-wider">
              {formatTime(currentTime)}
            </div>
            <div className="text-xs text-white/60 font-medium">
              {formatDate(currentTime)}
            </div>
          </div>
        </div>

        {/* Center Section - Vehicle Status */}
        <div className="flex items-center space-x-1">
          <div className="px-3 py-1 rounded-full bg-green-500/10 border border-green-400/30">
            <span className="text-green-400 text-sm font-medium">READY</span>
          </div>
          <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
        </div>

        {/* Right Section - Connection Status & Controls */}
        <div className="flex items-center space-x-3">
          
          {/* Signal Strength */}
          <div className="flex items-center space-x-1">
            <Signal className={`w-5 h-5 ${connectionStatus.signal > 2 ? 'text-green-400' : 'text-orange-400'}`} />
            <div className="flex space-x-1">
              {[...Array(4)].map((_, i) => (
                <div
                  key={i}
                  className={`w-1 h-3 rounded-full ${
                    i < connectionStatus.signal
                      ? 'bg-green-400'
                      : 'bg-white/20'
                  }`}
                />
              ))}
            </div>
          </div>

          {/* WiFi Status */}
          <button
            onClick={() => toggleConnection('wifi')}
            className={`
              p-2 rounded-xl transition-all duration-300 touch-scale
              ${connectionStatus.wifi
                ? 'bg-cyan-500/10 border border-cyan-400/30 text-cyan-400 hover:shadow-[0_0_10px_rgba(0,245,255,0.5)]'
                : 'bg-red-500/10 border border-red-400/30 text-red-400 hover:shadow-[0_0_10px_rgba(255,0,0,0.5)]'
              }
            `}
          >
            {connectionStatus.wifi ? (
              <Wifi className="w-5 h-5" />
            ) : (
              <WifiOff className="w-5 h-5" />
            )}
          </button>

          {/* Bluetooth Status */}
          <button
            onClick={() => toggleConnection('bluetooth')}
            className={`
              p-2 rounded-xl transition-all duration-300 touch-scale
              ${connectionStatus.bluetooth
                ? 'bg-blue-500/10 border border-blue-400/30 text-blue-400 hover:shadow-[0_0_10px_rgba(0,102,255,0.5)]'
                : 'bg-red-500/10 border border-red-400/30 text-red-400 hover:shadow-[0_0_10px_rgba(255,0,0,0.5)]'
              }
            `}
          >
            {connectionStatus.bluetooth ? (
              <BluetoothConnected className="w-5 h-5" />
            ) : (
              <Bluetooth className="w-5 h-5" />
            )}
          </button>

          {/* Battery Indicator */}
          <div className="flex items-center space-x-2">
            <Battery className="w-5 h-5 text-green-400" />
            <div className="w-12 h-2 bg-gray-700 rounded-full overflow-hidden">
              <div className="w-4/5 h-full bg-green-400 rounded-full"></div>
            </div>
            <span className="text-green-400 text-sm font-medium">85%</span>
          </div>

          {/* Dark Mode Toggle */}
          <button
            onClick={toggleDarkMode}
            className={`
              p-2 rounded-xl transition-all duration-300 touch-scale
              ${isDarkMode
                ? 'bg-purple-500/10 border border-purple-400/30 text-purple-400 hover:shadow-[0_0_10px_rgba(168,85,247,0.5)]'
                : 'bg-orange-500/10 border border-orange-400/30 text-orange-400 hover:shadow-[0_0_10px_rgba(255,107,53,0.5)]'
              }
            `}
          >
            {isDarkMode ? (
              <Moon className="w-5 h-5" />
            ) : (
              <Sun className="w-5 h-5" />
            )}
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;