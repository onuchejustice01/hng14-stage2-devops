# ---- Stage 1: Build ----
FROM node:18-alpine AS builder

WORKDIR /app

COPY package.json .
RUN npm install

COPY . .

# ---- Stage 2: Runtime ----
FROM node:18-alpine

WORKDIR /app

COPY --from=builder /app /app

# Use non-root user
USER node

EXPOSE 3000

# Healthcheck
HEALTHCHECK CMD wget --no-verbose --spider http://localhost:3000 || exit 1

CMD ["node", "app.js"]
