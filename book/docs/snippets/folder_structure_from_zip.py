import pathlib
import os
import zipfile

def folder_structure_from_zip(
    fpth_zip,
    fdir_dstn: pathlib.Path = pathlib.Path("."),
    new_name=None,
):
    if not fdir_dstn.exists():
        fdir_dstn.mkdir()
    else:
        pass

    copyto = fdir_dstn / fpth_zip.stem
    if copyto.exists():
        raise ValueError(f"cannot copy to {str(copyto)} as directory already exists")

    if new_name is not None:
        renameto = fdir_dstn / new_name
        if renameto.exists():
            raise ValueError(f"cannot copy to {str(copyto)} as already exists")

    with zipfile.ZipFile(fpth_zip, "r") as zip_ref:
        zip_ref.extractall(fdir_dstn)

    if new_name is not None:
        os.rename(copyto, renameto)
        return renameto
    else:
        return copyto