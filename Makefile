BRANCH = $(shell git rev-parse --abbrev-ref HEAD)

publish:
	git push origin $(BRANCH)
	git checkout gh-pages
	git merge $(BRANCH)
	git push origin gh-pages
	git checkout $(BRANCH)
