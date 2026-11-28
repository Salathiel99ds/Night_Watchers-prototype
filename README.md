
# Night Watchers Prototype 

> "Este projeto é a primeira materialização de algo com que eu já sonhava há muito tempo..."

Night Watchers é um jogo 2D desenvolvido em Python com Pygame para a disciplina de Introdução à Programação (2026.2) do Centro de Informática da Universidade Federal de Pernambuco (CIn-UFPE).

O jogo foi idealizado por José Salathiel e desenvolvido em conjunto com João Marcelo, Francisco Gabriel, João Moinhos e Rafael Ferreira.

## Sobre o jogo

O protótipo adapta um pequeno trecho do universo de Night Watchers, mais especificamente do seu Arco Brasileiro, em que Levi entra em conflito com o Flagelo Fulgurante, um dos onze Pivôs, grupo seleto que representa as grandes potências contemporâneas.

A história se passa em Recife, tendo como principais cenários o Centro de Informática da UFPE e o Marco Zero. Durante a exploração, o jogador encontra objetos que contribuem tanto para a progressão do jogo quanto para a compreensão dos acontecimentos da narrativa.

A ideia é apresentar parte desse universo por meio de uma experiência interativa, conciliando os conhecimentos adquiridos durante a disciplina com elementos de narrativa, ambientação e design de personagens.

## Jogabilidade

O jogador controla Levi em um ambiente 2D, podendo explorar diferentes cenários, interagir com objetos e acompanhar o desenvolvimento da história.

- Resolução de 960 × 540 pixels.
- Limite de 144 FPS.
- Movimentação com sprites direcionais.
- Colisões com paredes, obstáculos e limites dos cenários.
- Transições entre ambientes interligados.
- Sistema de coleta e interação com objetos.
- Cutscenes e diálogos relacionados à narrativa.
- Telas de início, tutorial, vitória e derrota.

## Objetos coletáveis

Diferentemente de coletáveis utilizados apenas para aumentar a pontuação do jogador, os objetos de Night Watchers possuem funções relacionadas ao desenvolvimento da história.

| Coletável | Função |
| :--- | :--- |
| Crachá | Permite que Levi tenha acesso ao interior do CIn. |
| Jornal | Apresenta informações sobre a situação política e institucional do Brasil dentro do universo do jogo. |
| Smartphone | Revela mensagens que ajudam a contextualizar os acontecimentos da narrativa. |

A obtenção de cada objeto é registrada por meio de variáveis booleanas, utilizadas para controlar a progressão e impedir que uma mesma coleta ocorra repetidamente.

A exibição individual das quantidades coletadas encontra-se em desenvolvimento.

## Cenários

Os ambientes foram desenvolvidos com base em locais reais, adaptados às necessidades do jogo e às limitações de uma representação bidimensional.

Atualmente, a exploração do Centro de Informática é dividida nos seguintes ambientes:

- Exterior do CIn;
- Entrada;
- Hall;
- Corredor 1;
- Jardim interno;
- Corredor 2;
- Grad05.

O Hall funciona como ponto de conexão entre diferentes partes do edifício. A presença de obstáculos em determinadas passagens faz com que o jogador explore caminhos alternativos.

Além dos ambientes do CIn, o projeto conta com o desenvolvimento de uma representação noturna do Marco Zero do Recife, local previsto para o encerramento do segmento narrativo adaptado.

## Capturas de tela

### Menu inicial e tutorial


### Ambientes do CIn



### Personagens e cutscenes



### Marco Zero


## Arquitetura e organização do projeto

O código foi dividido em diferentes arquivos para facilitar a organização, a manutenção e o desenvolvimento simultâneo das funcionalidades pelos integrantes da equipe.

```text
Night_Watchers-prototype/
├── assets/
├── personagens/
│   └── jogador.py
├── Cutscenes/
│   └── Cut_scene_grad05.py
├── main.py
├── mapa.py
├── Marco_Zero.py
├── game_over.py
├── tela_start.py
├── tela_tutorial.py
├── tela_vitoria.py
├── .gitignore
└── README.md
```

### Principais arquivos

- **main.py:** responsável pela inicialização do jogo, pelo loop principal, pelo gerenciamento dos estados, pelos coletáveis e pelas transições entre os ambientes.

- **mapa.py:** reúne os cenários do Centro de Informática, incluindo a representação dos ambientes e a definição das áreas de colisão.

- **personagens/jogador.py:** responsável pela movimentação e representação do personagem controlado pelo jogador.

- **Marco_Zero.py:** arquivo destinado à construção do cenário do Marco Zero e à sua futura integração com o restante do jogo.

- **Cutscenes:** diretório destinado às sequências narrativas, incluindo a cutscene da Grad05.

- **tela_start.py, tela_tutorial.py, tela_vitoria.py e game_over.py:** arquivos responsáveis pelas diferentes interfaces do jogo.

- **assets:** diretório destinado ao armazenamento dos recursos gráficos e audiovisuais utilizados no projeto.

## Como executar

É necessário possuir Python 3 instalado no computador.

Clone o repositório:

```bash
git clone https://github.com/Salathiel99ds/Night_Watchers-prototype.git
```

Acesse a pasta do projeto:

```bash
cd Night_Watchers-prototype
```

Instale a biblioteca Pygame:

```bash
python -m pip install pygame
```

Execute o arquivo principal:

```bash
python main.py
```

## Conceitos da disciplina aplicados

Durante o desenvolvimento do Night Watchers, foram utilizados diversos conceitos abordados ao longo da disciplina de Introdução à Programação.

- **Condicionais:** utilizadas nas verificações de colisão, coleta de objetos, transições entre cenários e mudanças de estado do jogo.

- **Laços de repetição:** utilizados no loop principal, no processamento dos eventos e na renderização dos elementos presentes nos cenários.

- **Listas e tuplas:** utilizadas para armazenar obstáculos, mensagens, coordenadas, dimensões e cores.

- **Variáveis booleanas:** utilizadas para registrar a obtenção dos coletáveis e controlar a execução de determinados eventos.

- **Funções e métodos:** utilizados para separar as responsabilidades de movimentação, atualização, renderização e processamento de eventos.

- **Programação Orientada a Objetos:** aplicada na construção das classes responsáveis pelo jogador, mapas, interfaces, cutscenes e gerenciamento do jogo.

- **Modularização:** utilizada para distribuir o código em diferentes arquivos, facilitando sua manutenção e integração.

### Exemplos de aplicação

Registro do estado dos coletáveis:

```python
self.tem_cracha = False
self.tem_jornal = False
self.smartphone_lido = False
```

Verificação da coleta do crachá:

```python
if jogador_rect.colliderect(self.cracha):
    self.tem_cracha = True
```

Controle temporal dentro do loop principal:

```python
dt = self.relogio.tick(self.fps) / 1000
```

Inicialização do jogo por meio da classe principal:

```python
if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()
```

## Desafios, erros e lições aprendidas

### Construção dos cenários e transições

Um dos maiores desafios encontrados durante o desenvolvimento foi a construção dos ambientes do Centro de Informática e a integração das passagens entre eles.

Em determinados momentos, o personagem era reposicionado incorretamente após atravessar uma passagem, retornava para um ambiente diferente do esperado ou ficava impossibilitado de prosseguir.

Para solucionar esses problemas, foi necessário revisar as condições de transição, as coordenadas de entrada e saída e a atualização das áreas de colisão de cada cenário.

### Integração dos coletáveis

A implementação dos objetos exigiu que o sistema de coleta estivesse relacionado à progressão do jogo. O crachá, por exemplo, precisava ser registrado antes que o personagem pudesse acessar o interior do edifício.

A utilização de variáveis booleanas permitiu controlar essas condições e evitar a repetição indevida das interações.

### Sprites e movimentação

Outro desafio foi a integração das sprites direcionais com a movimentação do personagem.

As diferenças entre as dimensões das imagens e das áreas de colisão exigiram ajustes para manter a representação visual do personagem alinhada ao seu comportamento dentro dos cenários.

### Utilização do GitHub

A utilização do GitHub também apresentou dificuldades durante o desenvolvimento, principalmente na integração de funcionalidades produzidas em branches diferentes.

Em algumas situações, alterações realizadas simultaneamente ocasionaram conflitos, tornando necessária a recuperação de versões anteriores e a revisão dos arquivos antes da integração.

Essas dificuldades contribuíram para uma melhor compreensão do controle de versões e da importância da comunicação entre os integrantes.

### Adaptação da narrativa

Por se tratar da adaptação de um universo narrativo mais amplo, foi necessário estabelecer quais elementos poderiam ser desenvolvidos dentro do escopo da disciplina.

Parte da história original precisou ser condensada ou adaptada, buscando preservar sua identidade sem comprometer a viabilidade técnica do protótipo.

## Divisão das responsabilidades

| Integrante | Responsabilidades |
| :--- | :--- |
| **José Salathiel** | Idealização do projeto, desenvolvimento da narrativa, estrutura principal do código, construção dos cenários, colisões, transições, coletáveis e resolução de problemas durante a integração. |
| **João Marcelo** | Desenvolvimento do código, correção de erros, implementação da tela de derrota, auxílio na documentação e preparação da apresentação. |
| **Francisco Gabriel** | Criação e integração das sprites, movimentação direcional, recursos gráficos, fontes, ajustes nas interfaces e organização dos arquivos de imagem. |
| **João Moinhos** | Desenvolvimento do código, criação e integração do menu inicial, tutorial, tela de derrota, produção de sprites e correção de falhas. |
| **Rafael Ferreira** | Desenvolvimento do código, implementação dos recursos sonoros, criação da interface de vitória, integração da tela de conclusão, documentação e preparação da apresentação. |

Além das responsabilidades individuais, os integrantes colaboraram na correção de erros, nos testes e na integração das diferentes partes do jogo.

---

Projeto desenvolvido pela Equipe 5 para a disciplina de Introdução à Programação — CIn/UFPE, 2026.2.
. 
