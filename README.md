# postbox

Write-only HTTP POST file storage.

Useful for:

* RPis sending pictures every 5 minutes to a storage server over unreliable WAN
  connections, where SSHFS does not work well.

* Having your friends send you files using their browser.

## Usage

1. `POST` to `/your-dir/your-file.ext` to upload a file.

   `curl http://127.0.0.1:8071/today/pic.jpg -F 'file=@pic.jpg'`

1. Refer your friends to `http://YO.UR.IP.ADDR:8071/`
