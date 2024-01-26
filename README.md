# Sports Streaming

[![Presentation](https://99freelas.s3-sa-east-1.amazonaws.com/portfolios/imagens/original/1641617/8df80bcb-2332-4b91-bfc4-dbf45ff83f9a/screenshot.png?id=4032213&token=8df80bcb-2332-4b91-bfc4-dbf45ff83f9a&nome=screenshot&type=.png)](https://www.youtube.com/watch?v=JjfII8XlpCo)

Site para streaming de jogos diversos: Futebol, Tênis, Basquete, etc.

# Instalação

Crie um arquivo chamado `.config.toml` e coloque o seguinte:

```
DOMAIN = "http://localhost:5000"
```

Onde `DOMAIN` é o dominio onde a aplicação vai rodar, no exemplo vai rodar em localhost.

Siga o script para rodar:

```
git clone https://github.com/riguima/sports-streaming
cd sports-streaming
pip install -r requirements.txt
gunicorn -b 0.0.0.0:5000 app:app
```

Acesse `http://localhost:5000/` para acessar os jogos.
