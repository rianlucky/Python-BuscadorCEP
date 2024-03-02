# Buscador de CEP usando API ViaCep

![Imagem da In](URL_da_Imagem)

Este programa é um buscador de CEP simples que utiliza a API ViaCep para obter informações sobre endereços no Brasil. O usuário fornece o número do CEP como entrada, e o programa retorna as seguintes informações: Logradouro, Bairro, Cidade e Estado (UF).

## Instruções de Uso

1. Certifique-se de ter o Python instalado em seu sistema. Se não tiver, você pode baixá-lo em [python.org](https://www.python.org/).
2. Clone ou baixe este repositório em sua máquina local.
3. Certifique-se de ter uma conexão com a Internet ativa para acessar a API ViaCep.
4. Navegue até o diretório onde os arquivos estão localizados.
5. Abra o terminal ou prompt de comando.
6. Execute o programa com o seguinte comando:

   ```bash
   python buscadorCep.py
   ```
7. Ira abrir uma interface gráfica para o usuario.
7. No campo em branco, insira o número do CEP que deseja pesquisar e clique Buscar.
8. O programa irá processar as informações e exibirá o Logradouro, Bairro, Cidade e Estado (UF) correspondentes ao CEP fornecido.

## Observações

- O programa pode lidar com diferentes formatos de CEP (com ou sem traços, espaços e pontos), mas é recomendável inserir apenas números para evitar erros.
- Este programa utiliza a API pública ViaCep, portanto, a disponibilidade das informações está sujeita à disponibilidade da API.

## Dependências

- Este programa utiliza o modulo Requests, então é aconselhavél a instalação do mesmo, conforme abaixo:
   ```bash
   pip install resquests
   ```

## Autor

- Este programa foi desenvolvido por Rian Lucas.

## Agradecimentos

- Agradecemos à equipe do ViaCep por fornecer uma API gratuita e confiável para busca de informações de endereço por CEP.
