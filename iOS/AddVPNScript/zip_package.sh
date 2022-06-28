cd "$(dirname "$0")"
echo "Current Directory $PWD"
rm ArchiveAddVPN1.zip
ls -ls ArchiveAddVPN1.zip
zip -r ArchiveAddVPN1.zip . \
-x Archive*.zip
ls -lst ArchiveAddVPN1.zip
date