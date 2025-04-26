
namespace TestExploringActions
{
    public class UnitTest1
    {
        [Fact]
        public void Test1()
        {
            // Arrange
            var controller = new ValuesController();

            // Act
            var result = controller.Get();

            // Assert
            Assert.NotNull(result);
        }
    }

    internal class ValuesController
    {
        public ValuesController()
        {
        }

        internal object? Get()
        {
            throw new NotImplementedException();
        }
    }
}