function BlogCard(props) {
    var hover = {':hover': {boxShadow: 20,}, display: { xs: 'block', sm:'block', md: 'flex', lg:'flex', xl:'flex'}  }
    var sxBoxContent = { 
                          display: { xs: 'block', sm:'block', md: 'flex', lg:'flex', xl:'flex'},
                          flexDirection: { xs: 'row', sm: 'row', md: 'column', lg:'column', xl:'column'}
                        }
    var sxCardMedia = { width: {  md: 151, lg: 151,  xl:151 } }
      return (
        <Card sx={hover}>
          {props.imagePage === null || props.imagePage === "" || props.imagePage === undefined ? null : 
          <CardMedia
            component="img"
            sx={sxCardMedia}
            image={props.imagePage}
            alt="Image"
          />
          }
          <Box sx={sxBoxContent}>
          <CardContent>
            <Typography gutterBottom variant="h5" component="div">
              {props.title}
            </Typography>
            <Typography variant="body2" color="text.secondary" component="div">{props.intro}</Typography>
            <Typography variant="caption" color="text.secondary" component="div">{props.date}</Typography>
          </CardContent>
          <CardActions>
          {props.link === "" || props.link === null || props.link === undefined ? null : <Button size="small" href={props.link} >Ir</Button>}
          </CardActions>
          </Box>

          
          
        </Card>
      );
    }