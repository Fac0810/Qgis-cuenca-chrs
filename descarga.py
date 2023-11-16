from chrs_persiann import CHRS
import io

#sacado de la pagina principal de chrs_persiann

def main():


    params = {
        'start': '2011010100',
        'end': '2011010300',
        'mailid': 'test@gmail.com',
        'download_path': 'persiann_descargado',
        'file_format': 'Tif',
        'timestep': 'daily',
        'compression': 'zip'
    }

    dl = CHRS()

    # PERSIANN CDR
    dl.get_persiann_cdr(**params)


    pass


if __name__ == '__main__':
    main()
