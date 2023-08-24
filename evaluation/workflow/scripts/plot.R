suppressPackageStartupMessages({
    library(dplyr)
    library(ggplot2)
    library(reshape2)
})


main <- function(snakemake) {
    df <- read.csv(snakemake@input[[1]]) %>%
        transmute(Method = method, Dataset = dataset, MSE = mse, R2 = r2) %>%
        melt(
            value.vars = c("MSE", "R2"),
            value.name="Score",
            variable.name="Metric",
        )
    gp <- ggplot(df, aes(x = Method, y = Score, fill = Method)) +
        geom_bar(stat = "identity") +
        facet_grid(Metric ~ Dataset, labeller = label_both, scales = "free_y") +
        theme_bw()
    ggsave(snakemake@output[[1]], gp, width = 7, height = 7)
}


main(snakemake)
