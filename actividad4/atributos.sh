archivo="$1"

permisos=$(stat -C "%a" "Sarchivo")
usuanto-$(stat -C "% "Sanchivo")
grupo-#(stat -c "%G* "$archivo")
tamano=$(stat -c "%s" "$archivo")
fecha-$(stat -c "%y" "archivo")
nombre=$(basename "§archivo")
exec > atributosinfo.txt
echo "Permisos: $permisos"
echo "Usuario: Susuario"
echo "Grupo: $grupo"
echo "Tamaño: $tamano bytes"
echo "Fecha y Hora: $fecha"
echo "Nombre del Archivo: Snombre"
echo "Infornación guardada en atributosinfo.txt"
echo “Uriel Alejandro Hernandez Hernandez - t05054562 - $(date +%F)*

