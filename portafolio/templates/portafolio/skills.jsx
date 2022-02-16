function SkillsCard(props) {
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
          <Typography variant="body2" color="text.secondary" component="div">{props.initDate === "" || props.initDate === null || props.initDate === undefined ? null: "Desde: "+props.initDate } </Typography>
          <Typography variant="body2" color="text.secondary" component="div">{props.endDate === "" || props.endDate === null || props.endDate === undefined ? null: "Hasta: "+props.endDate}  </Typography>
          <Typography component="div">
            {props.custom}
          </Typography>
        </CardContent>
        <CardActions>
        {props.link === "" || props.link === null || props.link === undefined ? null : <Button size="small" href={props.link} target="_blank">Ver más</Button>}
        </CardActions>
      </Card>
    );
  }