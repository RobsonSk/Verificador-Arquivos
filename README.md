# Verificador-Arquivos

Este repositório contém um script Python que registra detalhes sobre arquivos em diretórios especificados. Ele grava informações como tamanho do arquivo, data de modificação e extensão em um arquivo de log CSV, enquanto erros encontrados durante o processo são escritos em um arquivo de erro separado.

## Recursos
- **Registra detalhes dos arquivos, incluindo nome, tamanho, data de modificação e extensão.**
- **Lida com erros, gravando-os em um log de erros separado.**
- **Converte tamanhos de arquivos para formatos legíveis.**
- **Desenvolvido para Windows mas pode ser adaptado para ambientes UNIX.**

## Requisitos
```sh
Python 3.x
```

## Configuração
Clone este repositório para sua máquina local.
```sh
git clone https://github.com/RobsonSk/Verificador-Arquivos
```

Navegue até o diretório do repositório.
```sh
cd Verificador-Arquivos
```

Certifique-se de ter a estrutura de diretórios necessária e atualize os caminhos no script:
- **Atualize LogFile com o caminho desejado para seu arquivo de log.**
- **Atualize ErrorFile com o caminho desejado para seu arquivo de log de erros.**
- **Atualize o caminho do diretório em os.chdir(r'Diretorio\para\pesquisa') para o diretório que você deseja escanear.**

## Utilização
Execute o script usando Python:

```sh
python main.py
```
O script irá:

1. Mudar para o diretório especificado.
1. Listar todos os subdiretórios e iterar através deles.
1. Registrar detalhes de cada arquivo encontrado nesses diretórios no arquivo de log especificado.
1. Registrar quaisquer erros encontrados no arquivo de erro especificado.

## Funções internas
### convert_size(size_bytes)
Converte o tamanho de um arquivo em bytes para uma string legível.

### Parâmetros:
size_bytes (int): O tamanho do arquivo em bytes.

### Retorna:
str: Tamanho do arquivo legível.

### Fluxo do Script
1. Mudar Diretório:
- os.chdir(r'Diretorio\para\pesquisa'): Muda o diretório de trabalho atual para o caminho especificado.

1. Listar Diretórios:
- dirs = os.listdir(): Lista todos os diretórios no diretório de trabalho atual.

1. Iterar Sobre Diretórios:
- Para cada diretório, listar seu conteúdo e coletar detalhes dos arquivos.

1. Registrar Detalhes dos Arquivos:
- Para cada arquivo, coletar seu tamanho, data de modificação, nome e extensão.
- Gravar esses detalhes no arquivo de log.

1. Lidar com Erros:
- Exceções FileNotFoundError e NotADirectoryError são capturadas e registradas no arquivo de erro.

## Tratamento de Erros
O script registra quaisquer exceções FileNotFoundError ou NotADirectoryError no arquivo de log de erros com detalhes relevantes.

## Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENCE.md) para mais detalhes.

## Contato
Para qualquer pergunta ou sugestão, entre em contato com [Robson Scartezini](mailto:robsonshk@gmail.com).

