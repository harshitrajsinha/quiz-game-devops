# quiz-game-devops

* Since it uses input(), so the container needs to be run with `-it` (interactive + TTY) or it will fail waiting for input that never arrives.
```
    docker run -it <image>:<version>
```