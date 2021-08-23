import { app, BrowserWindow } from 'electron'
import { join } from 'path'
app.whenReady().then(() => {
  createWindow()
})
function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600, 
    frame: false
  })
  win.loadURL('http://localhost:8080/')
}