"""
GAIA v6.7 - Module principal du système de monitoring intelligent
"""

import asyncio
import time
from collections import deque
from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class Config:
    """Configuration du système GAIA"""
    max_history: int = 1000
    consciousness_threshold: float = 0.5
    threat_sensitivity: float = 0.8
    latency_window: int = 100


class GAIA:
    """
    Système de monitoring intelligent GAIA v6.7
    
    Surveille les métriques système et calcule un niveau de conscience
    basé sur les patterns détectés dans les données.
    """
    
    def __init__(self, config: Config):
        self.config = config
        self.cycle_count = 0
        self.consciousness = 0.0
        
        # Historique des métriques
        self.threats = deque(maxlen=config.max_history)
        self.latencies = deque(maxlen=config.latency_window)
        self.events_history = deque(maxlen=config.max_history)
        
        # État interne
        self._last_event_time = time.time()
        self._baseline_metrics = {"cpu": 0.5, "memory": 0.5, "network": 0.1}
    
    async def process_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Traite un événement de monitoring et met à jour l'état du système
        
        Args:
            event: Dictionnaire contenant les métriques (cpu, memory, network)
            
        Returns:
            Dictionnaire avec les résultats de l'analyse
        """
        start_time = time.time()
        
        # Validation des données d'entrée
        cpu = max(0.0, min(1.0, event.get("cpu", 0.5)))
        memory = max(0.0, min(1.0, event.get("memory", 0.5)))
        network = max(0.0, min(1.0, event.get("network", 0.0)))
        
        # Calcul du niveau de menace
        threat_level = self._calculate_threat_level(cpu, memory, network)
        
        # Mise à jour de l'historique
        self.threats.append(threat_level)
        self.events_history.append({
            "timestamp": start_time,
            "cpu": cpu,
            "memory": memory,
            "network": network,
            "threat": threat_level
        })
        
        # Calcul de la conscience
        self.consciousness = self._update_consciousness()
        
        # Calcul de la latence
        latency = (time.time() - start_time) * 1000  # en millisecondes
        self.latencies.append(latency)
        
        # Incrémentation du compteur de cycles
        self.cycle_count += 1
        self._last_event_time = time.time()
        
        return {
            "cycle": self.cycle_count,
            "threat_level": threat_level,
            "consciousness": self.consciousness,
            "latency_ms": latency,
            "status": "processed",
            "metrics": {
                "cpu": cpu,
                "memory": memory,
                "network": network
            }
        }
    
    def _calculate_threat_level(self, cpu: float, memory: float, network: float) -> float:
        """
        Calcule le niveau de menace basé sur les métriques système
        
        Args:
            cpu: Utilisation CPU (0-1)
            memory: Utilisation mémoire (0-1)
            network: Activité réseau (0-1)
            
        Returns:
            Niveau de menace (0-1)
        """
        # Calcul des déviations par rapport à la baseline
        cpu_deviation = abs(cpu - self._baseline_metrics["cpu"])
        memory_deviation = abs(memory - self._baseline_metrics["memory"])
        network_deviation = abs(network - self._baseline_metrics["network"])
        
        # Pondération des métriques
        weighted_threat = (
            cpu_deviation * 0.4 +
            memory_deviation * 0.4 +
            network_deviation * 0.2
        )
        
        # Application de la sensibilité
        threat_level = min(1.0, weighted_threat * self.config.threat_sensitivity)
        
        return threat_level
    
    def _update_consciousness(self) -> float:
        """
        Met à jour le niveau de conscience basé sur l'historique des menaces
        
        Returns:
            Niveau de conscience (0-1)
        """
        if len(self.threats) < 10:
            return 0.0
        
        # Calcul de la moyenne des menaces récentes
        recent_threats = list(self.threats)[-50:]  # 50 derniers événements
        avg_threat = sum(recent_threats) / len(recent_threats)
        
        # Calcul de la variance pour détecter l'instabilité
        variance = sum((t - avg_threat) ** 2 for t in recent_threats) / len(recent_threats)
        
        # Le niveau de conscience augmente avec l'activité et l'instabilité
        consciousness = min(1.0, (avg_threat + variance) * 1.5)
        
        # Lissage avec la valeur précédente
        if hasattr(self, 'consciousness'):
            consciousness = 0.8 * self.consciousness + 0.2 * consciousness
        
        return consciousness
    
    def get_status(self) -> Dict[str, Any]:
        """
        Retourne l'état actuel du système
        
        Returns:
            Dictionnaire avec l'état complet du système
        """
        return {
            "cycle_count": self.cycle_count,
            "consciousness": self.consciousness,
            "last_event": self._last_event_time,
            "threats_count": len(self.threats),
            "avg_threat": sum(self.threats) / len(self.threats) if self.threats else 0.0,
            "avg_latency": sum(self.latencies) / len(self.latencies) if self.latencies else 0.0,
            "config": {
                "max_history": self.config.max_history,
                "consciousness_threshold": self.config.consciousness_threshold,
                "threat_sensitivity": self.config.threat_sensitivity
            }
        }
    
    def reset(self):
        """Remet à zéro l'état du système"""
        self.cycle_count = 0
        self.consciousness = 0.0
        self.threats.clear()
        self.latencies.clear()
        self.events_history.clear()
        self._last_event_time = time.time()
