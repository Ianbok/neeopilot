import React, { useState, useEffect } from 'react';
import AppIcon from './AppIcon';
import { 
  Navigation, 
  Music, 
  Phone, 
  Settings, 
  Camera, 
  MessageCircle,
  Map,
  Radio,
  Thermometer,
  Car
} from 'lucide-react';

const HomeScreen = () => {
  const [activeApps, setActiveApps] = useState(['waze', 'spotify']);
  const [isLoaded, setIsLoaded] = useState(false);

  // Simulate loading animation
  useEffect(() => {
    const timer = setTimeout(() => {
      setIsLoaded(true);
    }, 300);
    return () => clearTimeout(timer);
  }, []);

  const appData = [
    {
      id: 'waze',
      label: 'Waze',
      icon: Navigation,
      color: 'cyan',
      isActive: activeApps.includes('waze')
    },
    {
      id: 'spotify',
      label: 'Spotify',
      icon: Music,
      color: 'green',
      isActive: activeApps.includes('spotify')
    },
    {
      id: 'phone',
      label: 'Phone',
      icon: Phone,
      color: 'blue',
      isActive: activeApps.includes('phone')
    },
    {
      id: 'messages',
      label: 'Messages',
      icon: MessageCircle,
      color: 'purple',
      isActive: activeApps.includes('messages')
    },
    {
      id: 'camera',
      label: 'Camera',
      icon: Camera,
      color: 'orange',
      isActive: activeApps.includes('camera')
    },
    {
      id: 'settings',
      label: 'Settings',
      icon: Settings,
      color: 'pink',
      isActive: activeApps.includes('settings')
    }
  ];

  const quickAccessData = [
    {
      id: 'maps',
      label: 'Maps',
      icon: Map,
      color: 'cyan'
    },
    {
      id: 'radio',
      label: 'Radio',
      icon: Radio,
      color: 'green'
    },
    {
      id: 'climate',
      label: 'Climate',
      icon: Thermometer,
      color: 'blue'
    },
    {
      id: 'vehicle',
      label: 'Vehicle',
      icon: Car,
      color: 'purple'
    }
  ];

  const handleAppClick = (appId) => {
    setActiveApps(prev => 
      prev.includes(appId) 
        ? prev.filter(id => id !== appId)
        : [...prev, appId]
    );
  };

  return (
    <div className="flex-1 p-6 overflow-hidden">
      {/* Main Apps Grid */}
      <div className="mb-8">
        <h2 className="text-xl font-bold text-white/90 mb-6 flex items-center">
          <div className="w-1 h-6 bg-cyan-400 rounded-full mr-3"></div>
          Main Applications
        </h2>
        
        <div className={`grid grid-cols-3 gap-6 justify-items-center ${isLoaded ? 'opacity-100' : 'opacity-0'} transition-opacity duration-1000`}>
          {appData.map((app, index) => (
            <AppIcon
              key={app.id}
              icon={app.icon}
              label={app.label}
              color={app.color}
              isActive={app.isActive}
              onClick={() => handleAppClick(app.id)}
              animationDelay={index * 100}
              size="large"
            />
          ))}
        </div>
      </div>

      {/* Quick Access Section */}
      <div className="mb-6">
        <h3 className="text-lg font-semibold text-white/80 mb-4 flex items-center">
          <div className="w-1 h-5 bg-green-400 rounded-full mr-3"></div>
          Quick Access
        </h3>
        
        <div className={`flex justify-center space-x-4 ${isLoaded ? 'opacity-100' : 'opacity-0'} transition-opacity duration-1000 delay-300`}>
          {quickAccessData.map((app, index) => (
            <AppIcon
              key={app.id}
              icon={app.icon}
              label={app.label}
              color={app.color}
              onClick={() => handleAppClick(app.id)}
              animationDelay={(appData.length * 100) + (index * 150)}
              size="medium"
            />
          ))}
        </div>
      </div>

      {/* Status Bar */}
      <div className={`mt-8 flex justify-center ${isLoaded ? 'opacity-100' : 'opacity-0'} transition-opacity duration-1000 delay-600`}>
        <div className="glass-effect rounded-2xl px-6 py-3 backdrop-blur-xl border border-white/10" style={{ backgroundColor: 'var(--bg-glass)' }}>
          <div className="flex items-center space-x-4 text-sm">
            <div className="flex items-center space-x-2">
              <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
              <span className="text-green-400 font-medium">System Online</span>
            </div>
            <div className="w-px h-4 bg-white/20"></div>
            <div className="text-white/60">
              {activeApps.length} apps running
            </div>
            <div className="w-px h-4 bg-white/20"></div>
            <div className="text-cyan-400 font-medium">
              NeeOPiloT v2.0
            </div>
          </div>
        </div>
      </div>

      {/* Background Decorative Elements */}
      <div className="fixed inset-0 pointer-events-none overflow-hidden -z-10">
        <div className="absolute top-1/4 left-1/4 w-64 h-64 bg-cyan-500/5 rounded-full blur-3xl"></div>
        <div className="absolute bottom-1/4 right-1/4 w-48 h-48 bg-green-500/5 rounded-full blur-3xl"></div>
        <div className="absolute top-1/2 right-1/3 w-32 h-32 bg-purple-500/5 rounded-full blur-2xl"></div>
      </div>
    </div>
  );
};

export default HomeScreen;