import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: '../wbackend/templates',
    emptyOutDir: true,
    rollupOptions: {
      output: {
        assetFileNames: 'static/[name].[hash][extname]'
      }
    }
  },
  server: {
    proxy: {
      '/weather': 'http://localhost:5022'  // For development only
    }
  }
})