# Publicar no GitHub — guia prático

Este projeto está **pronto como arquivos locais**; ele não cria uma conta, repositório remoto ou publicação automaticamente. Você deve autorizar o upload na sua conta.

## Opção 1 — Pelo navegador (mais simples)
1. Entre em https://github.com/new e autentique-se na sua conta.
2. Crie um repositório público chamado `jeanderson-santos-portfolio` (ou outro nome de sua preferência). Não marque a opção de criar README porque o pacote já contém um.
3. Abra o repositório e use **Add file → Upload files**. Envie **os arquivos e diretórios de dentro da pasta** `jeanderson-santos-portfolio` (não o ZIP compactado). Confira que `index.html` aparece na raiz.
4. Confirme o commit para a branch `main`.
5. Em **Settings → Pages → Build and deployment**, escolha **Deploy from a branch**, selecione **main** e **/(root)** e salve.
6. A URL do projeto será `https://berserk77720.github.io/jeanderson-santos-portfolio/`, após a publicação. Substitua `Berserk77720` pelo seu usuário real e ajuste o nome do repositório se necessário.

## Opção 2 — Usando Git no computador

Dentro da pasta extraída:

```bash
git init
git branch -M main
git add .
git commit -m "Portfolio: initial release"
git remote add origin https://github.com/Berserk77720/jeanderson-santos-portfolio.git
git push -u origin main
```

Crie antes um repositório vazio no GitHub. A autenticação é feita com os meios oficiais do GitHub (não coloque senhas em comandos ou arquivos).

## Se quiser GitHub Pages na URL principal
Use um repositório chamado `Berserk77720.github.io`. A URL será `https://berserk77720.github.io/`.

## Deixar o perfil do GitHub profissional
Para o README aparecer no perfil, crie um **segundo repositório**, público, cujo nome é exatamente seu usuário do GitHub. Copie o conteúdo de `profile/README.md` para o `README.md` desse segundo repositório; substitua `Berserk77720` e os links antes de publicar.

## Checklist de revisão obrigatória
- [ ] Confirmar se nome, email e resumo são os que você deseja tornar públicos.
- [ ] Checar títulos das empresas e informações sobre experiências, principalmente datas — não incluímos datas no site por existirem divergências entre documentos históricos.
- [ ] Revisar o texto dos casos profissionais para garantir autorização e ausência de dados de cliente.
- [ ] Revisar todo o conteúdo de `docs/` e os PDFs da pasta `resume/`.
- [ ] Não incluir arquivos da pasta privada, certificados sem ocultar dados pessoais ou currículos antigos.
- [ ] Abrir o site no celular após a publicação e testar os botões PT / EN.

**Referência oficial:** https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
