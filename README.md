# Sports Streaming

![](https://github.com/riguima/sports-streaming/blob/master/assets/presentation.mp4)

Site para streaming de jogos diversos: Futebol, Tênis, Basquete, etc.

# Instalação

Crie um arquivo chamado `.config.toml` e coloque o seguinte:

```
DOMAIN = "http://localhost:5000"
```

Onde `DOMAIN` é o dominio onde a aplicação vai rodar, no exemplo vai rodar em localhost.

Siga o script para rodar:

```
pip install -r requirements.txt
gunicorn -b 0.0.0.0:5000 app:app
```

Acesse `http://localhost:5000/` para acessar os jogos.
