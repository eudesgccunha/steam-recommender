# Steam Recommender

Construção de um modelo de recomendação de filtro colaborativo baseado em itens do dataset disponível da [Steam](https://www.kaggle.com/datasets/tamber/steam-video-games), seguido da construção de uma API para interagir com o modelo.

O objetivo é que o usuário informe um nome de jogo e receba como retorno os 10 jogos mais similares.

**Observação:** não há "avaliação/nota" (*rating*) direta dos jogos, de forma que é necessário calcular um *rating* implícito da seguinte pela seguinte fórmula: 

$$r_{\mathbf{ui}} = \frac{hours\ \mathbf{u}\ played\ in\ game\ \mathbf{i}}{total\ hours\ \mathbf{u}\ played}$$

ou seja, total de que o usuário jogou o game em relação ao total de horas jogadas em todos os jogos.



--- 
# Virtual env conda


```bash
conda create -n recommender python==3.12.4
conda activate recommender
pip install -r requirements.txt
```
