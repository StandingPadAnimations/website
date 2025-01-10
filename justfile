default: commit build deploy

# Deploy to server
deploy:
  rsync -avz --delete docs/ website@hetzner-reg:~/www

# Build in the Docs folder
build:
  hugo --destination docs
  npx tsx scripts/shikify.ts

build-and-preview: build preview-built 
preview-built: 
  npx http-server docs

# Preview
preview-real-time:
  hugo server --disableFastRender --destination docs

# Add and commit
commit:
  git add .
  git commit --signoff
