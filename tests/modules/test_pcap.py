"""
Unit tests for the PCAP analyzer.
"""

from pathlib import Path

from assistant.modules.pcap.service import PCAPAnalyzer


def test_pcap_analyzer() -> None:
    """
    Analyze a sample PCAP capture.
    """

    sample = Path("my_local_sample.pcap")

    assert sample.exists()

    result = PCAPAnalyzer.analyze(str(sample))

    assert result.path.endswith("my_local_sample.pcap")

    assert result.packet_count == 50

    assert "TCP" in result.protocols

    assert len(result.ipv4_addresses) >= 1

    assert "109.172.55.182" in result.ipv4_addresses

    assert "165.99.214.114" in result.ipv4_addresses

    assert "29.8.30.20" in result.ipv4_addresses
