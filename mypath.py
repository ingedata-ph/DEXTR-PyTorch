
class Path(object):
    @staticmethod
    def db_root_dir(database):
        if database == 'pascal':
            # folder that contains VOCdevkit/.
            return '/path/to/PASCAL/VOC2012'

        elif database == 'sbd':
            return '/path/to/SBD/'  # folder with img/, inst/, cls/, etc.
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def models_dir():
        return 'tools/annotation/dextr/models/'
