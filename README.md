# quiz-game-devops

* As it uses input(), the container needs to be run with `-it` (interactive + TTY) flag or it will fail waiting for input that never arrives.
```
    docker run -it <image>:<version>
```