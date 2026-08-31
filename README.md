# Laboratórios de Redes II — NS-2 e UDP

Os laboratórios abordam o funcionamento do protocolo **UDP (User Datagram Protocol)**, congestionamento, atraso de propagação, largura de banda e perda de pacotes.

## 📚 Laboratórios

### Laboratório 1 — Transferência de Dados com UDP

O primeiro laboratório apresenta o funcionamento básico do UDP em uma rede simulada, permitindo observar o comportamento dos pacotes em diferentes condições de tráfego.

**Principais objetivos:**

- Observar o funcionamento do protocolo UDP;
- Analisar os efeitos do congestionamento;
- Estudar atrasos de propagação;
- Avaliar o impacto da largura de banda no desempenho da rede;
- Identificar situações que podem provocar perda de pacotes.

**Arquivos principais:**

```text
Laboratorio_1/
├── arquivo1.nam
├── arquivo1.tr
├── lab_udp (1).docx
└── udp.tcl
```

---

### Laboratório 2 — Análise de Perda de Pacotes com UDP

O segundo laboratório aprofunda a análise do UDP em cenários com perda de pacotes. Além da simulação no NS-2, os resultados são analisados utilizando o **Wireshark**.

**Principais objetivos:**

- Analisar a perda de pacotes utilizando UDP;
- Compreender a influência do congestionamento e da latência;
- Avaliar os efeitos da largura de banda e da taxa de envio;
- Converter arquivos de trace do NS-2 para PCAP;
- Analisar os pacotes no Wireshark.

**Arquivos principais:**

```text
Laboratorio_2/
├── lab_udp2.docx
├── trace2pcap.py
├── udp-loss.nam
├── udp-loss.pcap
├── udp-loss.tcl
└── udp-loss.tr
```

## 🛠️ Tecnologias e ferramentas

- **NS-2 (Network Simulator 2)**
- **Tcl/Tk**
- **UDP**
- **CBR (Constant Bit Rate)**
- **Docker**
- **WSL (Windows Subsystem for Linux)**
- **Wireshark**
- **Python**
- **PCAP**

## 📁 Estrutura do repositório

```text
NS2_UDP/
│
├── Laboratorio_1/
│   ├── arquivo1.nam
│   ├── arquivo1.tr
│   ├── lab_udp (1).docx
│   └── udp.tcl
│
├── Laboratorio_2/
│   ├── lab_udp2.docx
│   ├── trace2pcap.py
│   ├── udp-loss.nam
│   ├── udp-loss.pcap
│   ├── udp-loss.tcl
│   └── udp-loss.tr
│
└── README.md
```

## 🚀 Como executar

Os laboratórios utilizam o ambiente Linux/WSL e o container Docker disponibilizado para o NS-2.

### Laboratório 1

No WSL, acesse a pasta:

```bash
cd /mnt/c/Users/celia/OneDrive/Documentos/Redes\ II/NS2_UDP/Laboratorio_1
```

Habilite o acesso ao display:

```bash
xhost +
```

Execute o container:

```bash
docker run --rm -it \
-e DISPLAY=$DISPLAY \
-v "$PWD:/ns2" \
-v /tmp/.X11-unix:/tmp/.X11-unix \
gelirettore/ns2
```

Dentro do container:

```bash
ns udp.tcl
```

### Laboratório 2

Acesse a pasta:

```bash
cd /mnt/c/Users/celia/OneDrive/Documentos/Redes\ II/NS2_UDP/Laboratorio_2
```

Execute o container:

```bash
docker run --rm -it \
-e DISPLAY=$DISPLAY \
-v "$PWD:/ns2" \
-v /tmp/.X11-unix:/tmp/.X11-unix \
gelirettore/ns2
```

Dentro do container:

```bash
ns udp-loss.tcl
```

## 📊 Experimentos

### Congestionamento

No Laboratório 1, a taxa de transmissão foi aumentada reduzindo o intervalo de envio dos pacotes CBR:

```tcl
$cbr set interval_ 0.002
$cbr1 set interval_ 0.003
```

O aumento da taxa de transmissão provocou maior ocupação das filas dos nós intermediários, especialmente na região entre os nós 2 e 3.

### Atraso de propagação

Foram avaliados diferentes valores de latência nos enlaces para observar como o atraso influencia o tempo necessário para os pacotes chegarem ao destino.

### Largura de banda

Foram comparados diferentes valores de capacidade dos enlaces, permitindo observar a relação entre largura de banda, congestionamento e perda de pacotes.

### Perda de pacotes

No Laboratório 2, foram realizados diferentes cenários de configuração:

| Cenário | Largura de banda | Intervalo CBR | Perda observada |
|---|---:|---:|---:|
| 1 | 2 Mb | 0,002 s / 0,003 s | 1286 pacotes |
| 2 | 5 Mb | 0,002 s / 0,003 s | 225 pacotes |
| 3 | 2 Mb | 0,005 s / 0,005 s | 92 pacotes |

Os experimentos mostraram que o aumento da largura de banda ou o aumento do intervalo entre os pacotes pode reduzir o congestionamento e, consequentemente, a quantidade de pacotes perdidos.

## 🦈 Análise com Wireshark

O Laboratório 2 também utiliza o script `trace2pcap.py` para converter o arquivo de rastreamento do NS-2:

```text
udp-loss.tr
```

em um arquivo:

```text
udp-loss.pcap
```

O arquivo PCAP pode então ser aberto no **Wireshark** para visualizar e analisar os pacotes gerados durante a simulação.

## 📌 Conclusões

Os experimentos realizados demonstraram que o desempenho de uma rede utilizando UDP é influenciado por fatores como:

- taxa de transmissão;
- largura de banda;
- atraso de propagação;
- congestionamento;
- capacidade das filas;
- perda de pacotes.

O UDP possui baixo overhead e não garante a entrega ou a ordem dos pacotes. Dessa forma, aplicações que necessitam de alta confiabilidade precisam utilizar mecanismos adicionais para detectar e tratar perdas, como confirmação de recebimento e retransmissão.

Por outro lado, aplicações nas quais **velocidade e baixa latência** são mais importantes que a garantia de entrega podem se beneficiar do uso do UDP.

---

**Disciplina:** Redes II  
**Tema:** Simulação e análise do protocolo UDP com NS-2
