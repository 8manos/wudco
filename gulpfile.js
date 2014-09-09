var gulp = require('gulp');
var sass = require('gulp-ruby-sass');
//var browserSync = require('browser-sync');
//var reload = browserSync.reload;

gulp.task('sass', function(){
	return gulp.src('content/css/main.sass')
		.pipe(sass({
			sourcemap: true
		}))
		.on('error', function(err){
			console.log(err.message);
		})
		.pipe(gulp.dest('content/css'));
		//.pipe(reload({stream:true}));
});

gulp.task('default', function(){
	/*browserSync({
		server: {
			baseDir: 'content'
		}
	});*/

	gulp.watch('content/css/*.sass', ['sass']);
});