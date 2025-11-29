FROM node:20

WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm

# Copy package files
COPY package.json pnpm-lock.yaml ./

# Install deps
RUN pnpm install

# Copy the rest of the project
COPY . .

EXPOSE 3000

CMD ["pnpm", "dev"]


