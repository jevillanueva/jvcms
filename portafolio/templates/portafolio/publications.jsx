function PublicationsCard(props) {
  var hover = {':hover': {boxShadow: 20,},}
    return (
      <Card sx={hover}>
        {props.image === null || props.image === "" || props.image === undefined ? null : 
        <CardMedia
          component="img"
          height="140"
          image={props.image}
          alt="Image"
        />
        }
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            {props.title}
          </Typography>
          <Typography variant="body2" color="text.secondary" component="div">{props.description}</Typography>
          <Typography component="div">
            {props.custom}
          </Typography>
        </CardContent>
        <CardActions>
        {props.link === "" || props.link === null || props.link === undefined ? null : <Button size="small" href={props.link} target="_blank">Ver</Button>}
        {props.document === "" || props.document === null || props.document === undefined ? null : <Button size="small" href={props.document} download>Archivo</Button>}
        </CardActions>
      </Card>
    );
  }