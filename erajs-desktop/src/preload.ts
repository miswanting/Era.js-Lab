import { app, BrowserWindow, screen } from 'electron'
import { join } from 'path'
app.whenReady().then(() => {
  createWindow()
})
const DefaultWindowSize = {
  width: 500,
  height: 600,
}
function createWindow() {
  const win = new BrowserWindow({
    width: 300,
    height: 100,
    frame: false,
    show: false,
    webPreferences: {
      preload: join(__dirname, 'dist/preload.js')
    }
  })
  win.once('ready-to-show', () => {
    win.show()
    // win.webContents.openDevTools()
    // setTimeout(() => {
    //   const screenSize = screen.getPrimaryDisplay().size
    //   win.setPosition((screenSize.width - DefaultWindowSize.width) / 2, (screenSize.height - DefaultWindowSize.height) / 2, true)
    //   win.setSize(DefaultWindowSize.width, DefaultWindowSize.height, true)
    // }, 2000)
  })
  win.loadURL('http://localhost:8080/')
}