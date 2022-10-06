import { makeStyles } from '@material-ui/core/styles';

export const styles = makeStyles((theme) => ({
    container: {
        display: 'flex',
        flexDirection: 'column',
        width: '100%',
        alignItems: 'center'
    },
    text: {
        marginInline: 10
    },
    select: {
        width: 200,
        marginTop: 10,
    }
}));