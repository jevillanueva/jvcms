function BlogFullCard(props) {
    var hover = {':hover': {boxShadow: 20,}, }
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
                
            <Typography gutterBottom variant="h5" component="div">{props.title}</Typography>
            <Typography variant="body2" color="text.secondary" component="div">{props.intro}</Typography>
            <Typography variant="caption" color="text.secondary" component="div">{props.date}</Typography>
            <Typography variant="body2" color="text.secondary" component="div">{props.body}</Typography>
            <Typography variant="body2" color="text.secondary" component="article" >{props.contentMarkdown}</Typography>
          </CardContent>
        </Card>
      );
    }