# fastapi-temp



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/topics/git/add_files/#add-files-to-a-git-repository) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin http://192.168.56.101/nikulin/fastapi-temp.git
git branch -M main
git push -uf origin main
```
### Установить GitLab Runner. Выполните на сервере:

```bash
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
sudo apt install -y gitlab-runner
```

```bash
sudo gitlab-runner register
```
### Машина VM2
```text
И далее будут вопросы — отвечайте так:

Enter the GitLab instance URL:
http://192.168.56.101/

Enter the registration token:
(вставьте токен из GitLab)

Enter a description for the runner:
runner-102

Enter tags (optional):
test

Enter an executor:
docker
docker:latest
```

```bash
sudo nano /etc/gitlab-runner/config.toml
```
```text
concurrent = 1
check_interval = 0
shutdown_timeout = 0

[session_server]
  session_timeout = 1800

[[runners]]
  name = "docker-host-runner"
  url = "http://192.168.56.101/"
  id = 9
  token = "glrtr-TCzqln3fiiJQr-kGBowWHW86MQpwOjEKdDozCw.01.121flyh6j"
  token_obtained_at = 2025-12-07T05:27:35Z
  token_expires_at = 0001-01-01T00:00:00Z
  executor = "docker"
  [runners.cache]
    MaxUploadedArchiveSize = 0
    [runners.cache.s3]
    [runners.cache.gcs]
    [runners.cache.azure]
  [runners.docker]
    tls_verify = false
    image = "docker:latest"
    privileged = false
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = [
    "/var/run/docker.sock:/var/run/docker.sock",
    "/cache"
  ]
    shm_size = 0
    network_mtu = 0

```
### Машина VM3 Deploy Runner

```text
Enter the GitLab instance URL:
http://192.168.56.101/

Enter the registration token:
(вставьте токен из GitLab)

Enter a description for the runner:
runner-103

Enter tags (optional):
deploy

Enter an executor:
shell
```
