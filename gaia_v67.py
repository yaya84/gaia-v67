#!/usr/bin/env python3
"""
GAIA v6.7 - Global Artificial Intelligence Assistant
Test and benchmark implementation
"""

import argparse
import asyncio
import json
import random
import time
from typing import Dict, List, Any


class Config:
    """Configuration class for GAIA system"""
    
    def __init__(self):
        self.max_consciousness = 1.0
        self.min_consciousness = 0.0
        self.threat_threshold = 0.8
        self.latency_target_ms = 100.0
        self.max_threats_history = 1000
        self.max_latencies_history = 1000


class GAIA:
    """Global Artificial Intelligence Assistant - Main processing engine"""
    
    def __init__(self, config: Config):
        self.config = config
        self.cycle_count = 0
        self.consciousness = 0.5  # Starting consciousness level
        self.threats: List[float] = []
        self.latencies: List[float] = []
        self._last_event_time = time.time()
    
    async def process_event(self, event: Dict[str, float]) -> Dict[str, Any]:
        """Process a system event and update internal state"""
        start_time = time.time()
        
        # Extract metrics from event
        cpu = event.get('cpu', 0.5)
        memory = event.get('memory', 0.5)
        network = event.get('network', 0.0)
        
        # Calculate threat level based on system metrics
        threat_level = self._calculate_threat_level(cpu, memory, network)
        self.threats.append(threat_level)
        
        # Limit threats history
        if len(self.threats) > self.config.max_threats_history:
            self.threats = self.threats[-self.config.max_threats_history:]
        
        # Update consciousness based on threat level and system state
        self._update_consciousness(threat_level)
        
        # Calculate and store latency
        end_time = time.time()
        latency_ms = (end_time - start_time) * 1000
        self.latencies.append(latency_ms)
        
        # Limit latencies history
        if len(self.latencies) > self.config.max_latencies_history:
            self.latencies = self.latencies[-self.config.max_latencies_history:]
        
        # Increment cycle count
        self.cycle_count += 1
        self._last_event_time = end_time
        
        # Return response
        return {
            "status": "processed",
            "cycle": self.cycle_count,
            "consciousness": self.consciousness,
            "threat_level": threat_level,
            "latency_ms": latency_ms,
            "timestamp": end_time
        }
    
    def _calculate_threat_level(self, cpu: float, memory: float, network: float) -> float:
        """Calculate threat level based on system metrics"""
        # Simple threat calculation - higher values indicate higher threat
        base_threat = (cpu + memory + network) / 3.0
        
        # Add some variability and non-linearity
        noise = random.uniform(-0.1, 0.1)
        threat = max(0.0, min(1.0, base_threat + noise))
        
        # Spike detection for unusual patterns
        if cpu > 0.9 or memory > 0.9:
            threat = min(1.0, threat * 1.5)
        
        return threat
    
    def _update_consciousness(self, threat_level: float):
        """Update consciousness level based on current threat and historical data"""
        # Consciousness decreases with higher threats
        threat_impact = -0.1 * threat_level
        
        # Add some recovery over time
        time_since_last = time.time() - self._last_event_time
        recovery = min(0.05, time_since_last * 0.01)
        
        # Update consciousness with bounds checking
        new_consciousness = self.consciousness + threat_impact + recovery
        self.consciousness = max(
            self.config.min_consciousness,
            min(self.config.max_consciousness, new_consciousness)
        )
    
    def get_status(self) -> Dict[str, Any]:
        """Get current system status"""
        return {
            "consciousness": self.consciousness,
            "cycle_count": self.cycle_count,
            "threats_count": len(self.threats),
            "latencies_count": len(self.latencies),
            "last_threat": self.threats[-1] if self.threats else 0.0,
            "last_latency": self.latencies[-1] if self.latencies else 0.0,
            "avg_threat": sum(self.threats) / len(self.threats) if self.threats else 0.0,
            "avg_latency": sum(self.latencies) / len(self.latencies) if self.latencies else 0.0
        }


async def run_tests() -> Dict[str, Any]:
    """Run validation tests for GAIA system"""
    config = Config()
    gaia = GAIA(config)
    
    test_results = {
        "test_suite": "GAIA v6.7 Validation",
        "timestamp": time.time(),
        "tests": []
    }
    
    # Test 1: Basic event processing
    try:
        event = {"cpu": 0.3, "memory": 0.4, "network": 0.1}
        result = await gaia.process_event(event)
        test_results["tests"].append({
            "name": "basic_event_processing",
            "status": "passed",
            "details": f"Processed event, cycle: {result['cycle']}, consciousness: {result['consciousness']:.3f}"
        })
    except Exception as e:
        test_results["tests"].append({
            "name": "basic_event_processing",
            "status": "failed",
            "error": str(e)
        })
    
    # Test 2: High threat scenario
    try:
        high_threat_event = {"cpu": 0.95, "memory": 0.9, "network": 0.8}
        result = await gaia.process_event(high_threat_event)
        threat_detected = result['threat_level'] > 0.7
        test_results["tests"].append({
            "name": "high_threat_detection",
            "status": "passed" if threat_detected else "failed",
            "details": f"Threat level: {result['threat_level']:.3f}, detected: {threat_detected}"
        })
    except Exception as e:
        test_results["tests"].append({
            "name": "high_threat_detection",
            "status": "failed",
            "error": str(e)
        })
    
    # Test 3: Multiple events processing
    try:
        for i in range(10):
            event = {
                "cpu": random.uniform(0.1, 0.8),
                "memory": random.uniform(0.1, 0.7),
                "network": random.uniform(0.0, 0.5)
            }
            await gaia.process_event(event)
        
        status = gaia.get_status()
        test_results["tests"].append({
            "name": "multiple_events_processing",
            "status": "passed",
            "details": f"Processed 10 events, final cycle: {status['cycle_count']}, consciousness: {status['consciousness']:.3f}"
        })
    except Exception as e:
        test_results["tests"].append({
            "name": "multiple_events_processing",
            "status": "failed",
            "error": str(e)
        })
    
    # Test 4: Consciousness bounds
    try:
        initial_consciousness = gaia.consciousness
        # Try to push consciousness to extremes
        for _ in range(5):
            await gaia.process_event({"cpu": 1.0, "memory": 1.0, "network": 1.0})
        
        final_consciousness = gaia.consciousness
        bounds_respected = 0.0 <= final_consciousness <= 1.0
        test_results["tests"].append({
            "name": "consciousness_bounds",
            "status": "passed" if bounds_respected else "failed",
            "details": f"Initial: {initial_consciousness:.3f}, Final: {final_consciousness:.3f}, Bounds OK: {bounds_respected}"
        })
    except Exception as e:
        test_results["tests"].append({
            "name": "consciousness_bounds",
            "status": "failed",
            "error": str(e)
        })
    
    # Calculate overall result
    passed_tests = sum(1 for test in test_results["tests"] if test["status"] == "passed")
    total_tests = len(test_results["tests"])
    test_results["summary"] = {
        "total_tests": total_tests,
        "passed": passed_tests,
        "failed": total_tests - passed_tests,
        "success_rate": passed_tests / total_tests if total_tests > 0 else 0.0
    }
    
    return test_results


async def run_benchmark(cycles: int = 1000) -> Dict[str, Any]:
    """Run performance benchmark for GAIA system"""
    config = Config()
    gaia = GAIA(config)
    
    start_time = time.time()
    
    benchmark_results = {
        "benchmark_suite": "GAIA v6.7 Performance",
        "timestamp": start_time,
        "cycles": cycles,
        "metrics": {}
    }
    
    # Run benchmark cycles
    for i in range(cycles):
        event = {
            "cpu": random.uniform(0.0, 1.0),
            "memory": random.uniform(0.0, 1.0),
            "network": random.uniform(0.0, 1.0)
        }
        await gaia.process_event(event)
    
    end_time = time.time()
    total_duration = end_time - start_time
    
    # Calculate metrics
    status = gaia.get_status()
    benchmark_results["metrics"] = {
        "total_duration_seconds": total_duration,
        "cycles_per_second": cycles / total_duration,
        "average_latency_ms": status["avg_latency"],
        "final_consciousness": status["consciousness"],
        "average_threat_level": status["avg_threat"],
        "total_cycles_processed": status["cycle_count"],
        "memory_efficiency": {
            "threats_stored": len(gaia.threats),
            "latencies_stored": len(gaia.latencies)
        }
    }
    
    return benchmark_results


def main():
    """Main entry point for command-line execution"""
    parser = argparse.ArgumentParser(description="GAIA v6.7 - Test and Benchmark Tool")
    parser.add_argument("--mode", choices=["test", "benchmark"], required=True,
                       help="Execution mode: test or benchmark")
    parser.add_argument("--cycles", type=int, default=1000,
                       help="Number of cycles for benchmark mode (default: 1000)")
    
    args = parser.parse_args()
    
    try:
        if args.mode == "test":
            results = asyncio.run(run_tests())
        elif args.mode == "benchmark":
            results = asyncio.run(run_benchmark(args.cycles))
        
        # Output results as JSON
        print(json.dumps(results, indent=2))
        
        # Exit with appropriate code for tests
        if args.mode == "test":
            success_rate = results.get("summary", {}).get("success_rate", 0.0)
            exit_code = 0 if success_rate >= 1.0 else 1
            exit(exit_code)
        
    except Exception as e:
        error_result = {
            "error": str(e),
            "mode": args.mode,
            "timestamp": time.time()
        }
        print(json.dumps(error_result, indent=2))
        exit(1)


if __name__ == "__main__":
    main()