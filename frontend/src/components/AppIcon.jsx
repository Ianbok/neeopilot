import React from 'react';

const AppIcon = ({ 
  icon: IconComponent, 
  label, 
  isActive = false, 
  onClick,
  color = 'cyan',
  size = 'large',
  animationDelay = 0 
}) => {
  const colorMap = {
    cyan: {
      bg: 'bg-cyan-500/10',
      border: 'border-cyan-400/30',
      text: 'text-cyan-400',
      hoverShadow: 'hover:shadow-[0_0_20px_rgba(0,245,255,0.7)]',
      activePulse: 'shadow-[0_0_15px_rgba(0,245,255,0.8)]'
    },
    green: {
      bg: 'bg-green-500/10',
      border: 'border-green-400/30',
      text: 'text-green-400',
      hoverShadow: 'hover:shadow-[0_0_20px_rgba(74,245,80,0.7)]',
      activePulse: 'shadow-[0_0_15px_rgba(74,245,80,0.8)]'
    },
    purple: {
      bg: 'bg-purple-500/10',
      border: 'border-purple-400/30',
      text: 'text-purple-400',
      hoverShadow: 'hover:shadow-[0_0_20px_rgba(168,85,247,0.7)]',
      activePulse: 'shadow-[0_0_15px_rgba(168,85,247,0.8)]'
    },
    orange: {
      bg: 'bg-orange-500/10',
      border: 'border-orange-400/30',
      text: 'text-orange-400',
      hoverShadow: 'hover:shadow-[0_0_20px_rgba(255,107,53,0.7)]',
      activePulse: 'shadow-[0_0_15px_rgba(255,107,53,0.8)]'
    },
    pink: {
      bg: 'bg-pink-500/10',
      border: 'border-pink-400/30',
      text: 'text-pink-400',
      hoverShadow: 'hover:shadow-[0_0_20px_rgba(255,0,110,0.7)]',
      activePulse: 'shadow-[0_0_15px_rgba(255,0,110,0.8)]'
    },
    blue: {
      bg: 'bg-blue-500/10',
      border: 'border-blue-400/30',
      text: 'text-blue-400',
      hoverShadow: 'hover:shadow-[0_0_20px_rgba(0,102,255,0.7)]',
      activePulse: 'shadow-[0_0_15px_rgba(0,102,255,0.8)]'
    }
  };

  const sizeMap = {
    small: {
      container: 'w-16 h-16',
      icon: 'w-6 h-6',
      text: 'text-xs',
      padding: 'p-3'
    },
    medium: {
      container: 'w-20 h-20',
      icon: 'w-8 h-8',
      text: 'text-sm',
      padding: 'p-4'
    },
    large: {
      container: 'w-24 h-24',
      icon: 'w-10 h-10',
      text: 'text-sm',
      padding: 'p-5'
    }
  };

  const colorClasses = colorMap[color];
  const sizeClasses = sizeMap[size];

  return (
    <div 
      className={`cascade-item flex flex-col items-center space-y-2 group cursor-pointer`}
      style={{ animationDelay: `${animationDelay}ms` }}
      onClick={onClick}
    >
      <div
        className={`
          ${sizeClasses.container} ${sizeClasses.padding}
          ${colorClasses.bg} ${colorClasses.border}
          backdrop-blur-xl border-2 rounded-2xl
          flex items-center justify-center
          transition-all duration-300 ease-out
          hover:scale-110 active:scale-95
          ${colorClasses.hoverShadow}
          ${isActive ? `${colorClasses.activePulse} pulse-active` : ''}
          glass-effect glass-hover touch-scale
          relative overflow-hidden
        `}
      >
        <div className="absolute inset-0 bg-gradient-to-br from-white/5 to-transparent rounded-2xl" />
        
        <IconComponent 
          className={`${sizeClasses.icon} ${colorClasses.text} relative z-10 group-hover:drop-shadow-lg`}
        />
        
        {isActive && (
          <div className={`absolute -top-1 -right-1 w-3 h-3 ${colorClasses.bg} ${colorClasses.border} rounded-full`}>
            <div className={`w-full h-full ${colorClasses.text.replace('text', 'bg')} rounded-full animate-ping opacity-75`} />
            <div className={`absolute inset-0 w-full h-full ${colorClasses.text.replace('text', 'bg')} rounded-full`} />
          </div>
        )}
      </div>
      
      <span className={`${sizeClasses.text} text-white/80 font-medium text-center leading-tight max-w-20`}>
        {label}
      </span>
    </div>
  );
};

export default AppIcon;