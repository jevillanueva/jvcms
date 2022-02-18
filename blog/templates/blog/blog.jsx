function BlogCard(props) {
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
            <Typography variant="body2" color="text.secondary" component="div">{props.intro}</Typography>
            <Typography variant="caption" color="text.secondary" component="div">{props.date}</Typography>
          </CardContent>
          <CardActions>
          {props.link === "" || props.link === null || props.link === undefined ? null : <Button size="small" href={props.link} target="_blank">Ir</Button>}
          </CardActions>
        </Card>
      );
    }