"""
EJEMPLOS:
	TOKEN = Token de la aplicacion
	RUTA_ARCHIVO_LOCAL = la ruta del archivo
			mas nombre del archivo
	RUTA_ARCHIVO_REMOTO = ruta de archivo en Dropbox
			mas nombre del archivo

"""

import dropbox

dbx = dropbox.Dropbox('TOKEN')

with open('<RUTA_ARCHIVO_LOCAL>', 'wb') as f:
	dbx.files_download_to_file("ARCHIVO_LOCAL", '/<RUTA_ARCHIVO_REMOTO>')
