
# Добавление официального репозитория GitLab

```bash
curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
```


# Установка GitLab Community Edition

```bash
sudo apt install gitlab-ce
```

```bash
sudo gitlab-ctl reconfigure
sudo gitlab-ctl restart
sudo gitlab-ctl status
```

```bash
sudo cat /etc/gitlab/initial_root_password
```
Если забыли пароль, можно сбросить командой:

```bash
sudo gitlab-rake "gitlab:password:reset[root]"
```
### 🔹 Разблокировка пользователя через консоль
```bash
sudo gitlab-rails console
```
```ruby
user = User.find_by(username: 'nikulin')
```
3. Активируйте учетную запись:
```ruby
user.activate
user.save
```
3. Выйдите из консоли:
`exit`


