using ExploringAccions;
using ExploringAccions.Controllers;
using Microsoft.Extensions.Logging;
using Moq;

namespace Testexploringaccions
{
    public class WeatherForecastControllercsUnitTest
    {
        [Fact]
        public void Test_WeatherForecastControllercsUnitTest()
        {
            // Arrange
            var logger = new Mock<ILogger<WeatherForecastController>>();
            var controller = new WeatherForecastController(logger.Object);

            // Act
            var result = controller.Get();

            // Assert
            Assert.NotNull(result);
            Assert.IsType<WeatherForecast[]>(result);
        }
    }
}