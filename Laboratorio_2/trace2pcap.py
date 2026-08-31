import sys
from scapy.all import *

def tr2pcap(tracefile, pcapfile):
    packets = []
    lost_packets = set()
    expected_packets = set()
    received_packets = set()

    with open(tracefile, "r") as f:
        for line in f:            
            fields = line.split()
            if len(fields) < 12:  # Verifica se a linha tem a quantidade mínima de campos
                continue
            
            event = fields[0]
            time = float(fields[1])
            from_node = fields[2]
            to_node = fields[3]
            pkt_type = fields[4]
            pkt_size = int(fields[5])
            flags = fields[6]
            fid = fields[7]
            src_addr = fields[8]
            dst_addr = fields[9]
            seq_num = fields[10]
            pkt_id = fields[11]

            # Adiciona todos os pacotes esperados
            expected_packets.add(pkt_id)

            # Considera pacotes recebidos para conversão
            if event == 'r' and pkt_type == 'cbr':
                src_ip = "10.0.0." + str(from_node)  # Converte node para um IP fictício
                dst_ip = "10.0.0." + str(to_node)
                payload = bytes(pkt_size)
                pkt = IP(src=src_ip, dst=dst_ip)/UDP(dport=5000, sport=4000)/Raw(load=payload)
                packets.append(pkt)
                received_packets.add(pkt_id)  # Marca o pacote como recebido                
            elif event == 'd' and pkt_type == 'cbr': 
               src_ip = "0.0.0.0"  # Usando um IP fictício para pacotes perdidos
               dst_ip = "255.255.255.255"  # Usando um IP fictício para pacotes perdidos
               payload = b'LOST_PACKET'
               pkt = IP(src=src_ip, dst=dst_ip)/UDP(dport=5000, sport=4000)/Raw(load=payload)
               packets.append(pkt)
               lost_packets.add(pkt_id)

    # Identifica pacotes perdidos
    #lost_packets = expected_packets - received_packets

    # Exibe os pacotes recebidos e perdidos
    print(f"Total de pacotes esperados: {len(expected_packets)}")
    print(f"Total de pacotes recebidos: {len(received_packets)}")
    print(f"Total de pacotes perdidos: {len(lost_packets)}")
    print(f"IDs dos pacotes perdidos: {lost_packets}")

    # Escreve os pacotes recebidos em um arquivo pcap
    wrpcap(pcapfile, packets)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 tr2pcap.py <tracefile> <pcapfile>")
        sys.exit(1)
    
    tr2pcap(sys.argv[1], sys.argv[2])
