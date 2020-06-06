you create one manually via .env.sample

or if you are a member, private env file be git clone here https://gitlab.com/namgivu/browserstack-secret
```bash
cd :browserstack_start/.env_vault/
    cd ./gitclone
        [[ ! -d ./browserstack-secret/ ]] && git clone git@gitlab.com:namgivu/browserstack-secret.git  \
                                        || (cd ./browserstack-secret/ && git pull)
    cd - 1>/dev/null
