var gulp = require('gulp');
var sass = require('gulp-ruby-sass');

gulp.task('sass', function(){
	return gulp.src('content/css/main.sass')
		.pipe(sass({
			sourcemap: true
		}))
		.on('error', function(err){
			console.log(err.message);
		})
		.pipe(gulp.dest('content/css'));
});

gulp.task('default', function(){
	gulp.start('sass');
	gulp.watch('content/css/*.sass', ['sass']);
});