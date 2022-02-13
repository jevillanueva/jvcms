function EmployCard(props) {
  var maxWidth = { maxWidth: 350 }
  console.log(props.link )
    return (
      <Card sx={maxWidth}>
        {props.image === null || props.image === "" || props.image === undefined ? null : 
        <CardMedia
          component="img"
          height="140"
          image={props.image}
          alt="green iguana"
        />
        }
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            {props.jobTitle}
          </Typography>
          <Typography variant="body2" color="text.secondary">{props.employer}</Typography>
          <Typography variant="body2" color="text.secondary">{props.city}</Typography>
          <Typography variant="body2" color="text.secondary" component="div">{props.description}</Typography>
          <Typography variant="body2" color="text.secondary" component="div">{props.initDate === "" || props.initDate === null || props.initDate === undefined ? null: "Desde: "+props.initDate } </Typography>
          <Typography variant="body2" color="text.secondary" component="div">{props.endDate === "" || props.endDate === null || props.endDate === undefined ? null: "Hasta: "+props.endDate}  </Typography>
        </CardContent>
        <CardActions>
        {props.link === "" || props.link === null || props.link === undefined ? null : <Button size="small" href={props.link} target="_blank">Ver más</Button>}
        {props.document === "" || props.document === null || props.document === undefined ? null : <Button size="small" href={props.document} download>Documento</Button>}
        </CardActions>
      </Card>
    );
  }