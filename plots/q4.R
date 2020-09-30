astar <- c(log(565), log(11674))
bfs <- c(log(565), log(16688))
dfs <- c(log(409), log(361))

colors <- c("blue", "green", "blue", "green", "blue", "green")

barplot(cbind(astar, bfs, dfs), beside = TRUE, names.arg = c("A*", "BFS", "DFS"), col = colors, ylim = c(0,10), main = "Comparison of A*, BFS, and DFS", ylab = "Logarithmic values")
legend("topright", legend = c("Score", "Expanded nodes"), col=c("blue", "green"), pch = c(15,15))

